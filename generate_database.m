clear all;

%% Initialize params

init_params;

%% Simulation parameters
step_time = 0.01; % Simulation step time
sim_time = 10;   % Simulation time in seconds

%% Generate time vector
time = 0:step_time:sim_time;

%% Tamanho do dataset
M = 1;
N = length(time);
signals = round(rand(M, N));  % Generating random binary values
outputs = zeros(M,2*N);
inputs = zeros(M, 2*N);

for m=1:M
    %% Open Simulink model
    model_name = 'gmaw_process';
    open_system(model_name);

    %% Setup Signal Builder block
    upper_value = fo; % Upper value for the binary signal
    lower_value = fo/2; % Lower value for the binary signal
    frequency = 10;   % Frequency of the binary signal (Hz)

    %% Generate a pseudo-random binary signal using the parameters
    f_signal = lower_value + (upper_value - lower_value) * (rand(size(time)) > 0.5);
    Ir_signal = ones(1, N)*Ir;
    inputs(m,:) = [f_signal Ir_signal];
  
    %% Setup Signal Builder block in the model
    signal_f_path = [model_name, '/Signal f']; % Update with your Signal Builder block's path
    signal_f_block = get_param(signal_f_path, 'Handle');
    % Set the generated binary signal using the 'set' function
    signalbuilder(signal_f_block, 'set', 1, 1, time, f_signal);

    %% Simulate
    % Define simulation options structure
    simOut = sim(model_name, 'FixedStep', num2str(step_time), 'StopTime', num2str(sim_time));

    tout = simOut.tout;
    we = simOut.we.Data;
    we = resample(we', tout, 1/step_time);
    h = simOut.h.Data;
    h = resample(h', tout, 1/step_time);

    % Generate Gaussian noise
    noise_mean = 0;      % Mean of the Gaussian noise
    noise_stddev = 1e-6;  % Standard deviation of the Gaussian noise
    gaussian_noise = noise_mean + noise_stddev * randn(size(time));
    
    we = we + gaussian_noise;
    h = h + gaussian_noise;
    
    outputs(m,:) = [we h];
    
    %% Plot
%     figure;
%     subplot(2,1,1);
%     plot(time, f_signal);
%     xlabel('t');
%     ylabel('f');
%     title('Input f');
%     subplot(2,1,2);
%     plot(time, Ir_signal);
%     xlabel('t');
%     ylabel('Ir');
%     title('Input Ir');
%     sgtitle('Inputs', 'FontSize', 16); % Adjust font size if needed

%     figure;
%     subplot(2,1,1);
%     plot(time, we);
%     xlabel('t');
%     ylabel('we');
%     title('Output we');
%     subplot(2,1,2);
%     plot(time, h);
%     xlabel('t');
%     ylabel('h');
%     title('Output h');
%     sgtitle('Outputs', 'FontSize', 16); % Adjust font size if needed
end

%% Save data
csvwrite('database/inputs.csv',inputs)
csvwrite('database/outputs.csv',outputs)
