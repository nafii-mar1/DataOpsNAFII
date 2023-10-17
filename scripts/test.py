def testing_data(model, t_data):
    # Evaluate the model on the test data
    test_loss, test_accuracy = model.evaluate(t_data[0], t_data[1])
    print(f'Test accuracy: {test_accuracy}')
    
    # Generate predictions
    predictions = (model.predict(t_data[0]) > 0.5).astype(int)
    
    # Calculate precision, recall, F1-score
    report = classification_report(t_data[1], predictions)
    print(report)
    
    return test_loss, test_accuracy