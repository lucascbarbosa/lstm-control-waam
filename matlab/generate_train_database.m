clear all;

%% Initialize params

init_params;

%% Simulation parameters
step_time = 0.1; % Simulation step time
sim_time = 1000;   % Simulation time in seconds

%% Generate time vector
time = 0:step_time:sim_time;

%% Tamanho do datase
n_inputs = 2;
n_outputs = 2;
N = length(time);
outputs = zeros(N, n_outputs);
inputs = zeros(N, n_inputs);

%% Open Simulink model
model_name = 'gmaw_process';
open_system(model_name);

%% Setup Signal Builder block
upper_value = fo; % Upper value for the binary signal
lower_value = fo/2; % Lower value for the binary signal

%% Generate a pseudo-random binary signal using the parameters
f_binary_signal = (rand(size(time)) > 0.5);
f_signal = lower_value + (upper_value - lower_value) * f_binary_signal;
Ir_binary_signal = ones(1, N);
Ir_signal = Ir_binary_signal * Ir;
inputs(:, 1) = f_binary_signal';
inputs(:,2) = Ir_binary_signal';

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

outputs(:,1) = we;
outputs(:,2) = h;

%% Plot
% figure;
% subplot(2,1,1);
% plot(time, f_signal);
% xlabel('t');
% ylabel('f');
% title('Input f');
% subplot(2,1,2);
% plot(time, Ir_signal);
% xlabel('t');
% ylabel('Ir');
% title('Input Ir');
% sgtitle('Inputs', 'FontSize', 16); % Adjust font size if needed
% 
% figure;
% subplot(2,1,1);
% plot(time, we);
% xlabel('t');
% ylabel('we');
% title('Output we');
% subplot(2,1,2);
% plot(time, h);
% xlabel('t');
% ylabel('h');
% title('Output h');
% sgtitle('Outputs', 'FontSize', 16); % Adjust font size if needed

%% Save data
% Define column headers
inputs_headers = {'f', 'Ir'};
outputs_headers = {'we', 'h'};

% Convert data array to a table
inputs_table = array2table(inputs, 'VariableNames', inputs_headers);
outputs_table = array2table(outputs, 'VariableNames', outputs_headers);

% Save data table to a CSV file
writetable(inputs_table, 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/train_inputs.csv');
writetable(outputs_table, 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/train_outputs.csv');