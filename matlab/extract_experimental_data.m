clc;
close all;

folderPath = 'C:\Users\lucas\OneDrive\Documentos\GitHub\lstm-control-waam\matlab\dados-experimento\mat\';
fileList = dir(fullfile(folderPath, '*.mat'));

for i = 1:numel(fileList)
    % Check if the current file is a .mat file
    if fileList(i).isdir == 0
        % Step 4: Load the .mat file
        matFileName = fullfile(folderPath, fileList(i).name);
        data = load(matFileName);
        
        width_array = zeros(data.i, 2);
        w_t = data.width_time;
        w = data.width_array;
        width_array(:,1) = w_t;
        width_array(:,2) = w;
        width_table = array2table(width_array, 'VariableNames', {'t','w'});
        writetable(width_table, ['C:\Users\lucas\OneDrive\Documentos\GitHub\lstm-control-waam\matlab\dados-experimento\csv\',fileList(i).name,'_w.csv']);

        wfs_t = data.powersource_state_time;
        wfs_array = zeros(length(wfs_t),2);
        wfs_array(:,1) = wfs_t;
        wfs_array(:,2) = data.wfs;
        wfs_table = array2table(wfs_array, 'VariableNames', {'t','wfs'});
        writetable(wfs_table, ['C:\Users\lucas\OneDrive\Documentos\GitHub\lstm-control-waam\matlab\dados-experimento\csv\',fileList(i).name,'_wfs.csv']);
    end
end

% writematrix(w_array, 'C:\Users\lucas\OneDrive\Documentos\GitHub\lstm-control-waam\matlab\dados-experimento\width.csv');
% writematrix(wfs_array, 'C:\Users\lucas\OneDrive\Documentos\GitHub\lstm-control-waam\matlab\dados-experimento\wfs.csv');