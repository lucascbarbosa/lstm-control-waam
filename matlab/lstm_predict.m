function prediction = lstm_predict(input_data,model_filename)
    model = importKerasNetwork(model_filename);
    prediction = predict(model, input_data);
end
