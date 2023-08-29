clear all;

%% Initialize params

init_params;

%% Simulation parameters
step_time = 0.00001; % Simulation step time
sim_time = 10;   % Simulation time in seconds

%% Generate time vector
time = 0:step_time:sim_time;

%% Tamanho do dataset de treino
n_inputs = 2;
n_outputs = 2;
N = length(time);
outputs = zeros(N, n_outputs);
inputs = zeros(N, n_inputs);

%% Open Simulink model
model_name = 'gmaw_process';
open_system(model_name);

%% Setup Signal Builder block
f_lv = 0*fo; % Lower value for the binary signal
f_uv = fo; % Upper value for the binary signal
Ir_lv = 0.6*Ir; % Lower value for the binary signal
Ir_uv = Ir; % Upper value for the binary signal

%% Generate a pseudo-random binary signal using the parameters
f_binary_signal = randi([0, 1], 1, N);
Ir_binary_signal = randi([0, 1], 1, N);

f_signal = f_lv + (f_uv - f_lv) * f_binary_signal;
Ir_signal = Ir_lv + (Ir_uv - Ir_lv) * Ir_binary_signal;

inputs(:, 1) = f_signal';
inputs(:,2) = Ir_signal';

%% Setup Signal Builder block in the model
signal_f_path = [model_name, '/Signal f']; % Update with your Signal Builder block's path
signal_f_block = get_param(signal_f_path, 'Handle');
% Set the generated binary signal using the 'set' function
signalbuilder(signal_f_block, 'set', 1, 1, time, f_signal);

signal_Ir_path = [model_name, '/Signal Ir']; % Update with your Signal Builder block's path
signal_Ir_block = get_param(signal_Ir_path, 'Handle');
% Set the generated binary signal using the 'set' function
signalbuilder(signal_Ir_block, 'set', 1, 1, time, Ir_signal);

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
% ylabel('Ir');
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

%% Generate a pseudo-random binary signal using the parameters

n_amplitudes = 10;
f_binary_signal = randi([0, n_amplitudes-1], 1, N)/(n_amplitudes-1);
Ir_binary_signal = randi([0, n_amplitudes-1], 1, N)/(n_amplitudes-1);

f_signal = f_lv + (f_uv - f_lv) * f_binary_signal;
Ir_signal = Ir_lv + (Ir_uv - Ir_lv) * Ir_binary_signal;

inputs(:, 1) = f_signal';
inputs(:,2) = Ir_signal';

%% Setup Signal Builder block in the model
signal_f_path = [model_name, '/Signal f']; % Update with your Signal Builder block's path
signal_f_block = get_param(signal_f_path, 'Handle');
% Set the generated binary signal using the 'set' function
signalbuilder(signal_f_block, 'set', 1, 1, time, f_signal);

signal_Ir_path = [model_name, '/Signal Ir']; % Update with your Signal Builder block's path
signal_Ir_block = get_param(signal_Ir_path, 'Handle');
% Set the generated binary signal using the 'set' function
signalbuilder(signal_Ir_block, 'set', 1, 1, time, Ir_signal);

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
% ylabel('Ir');
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
writetable(inputs_table, 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/test_inputs.csv');
writetable(outputs_table, 'C:/Users/lucas/OneDrive/Documentos/GitHub/lstm-control-waam/database/test_outputs.csv');
