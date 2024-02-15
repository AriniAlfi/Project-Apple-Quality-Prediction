This case study on apple quality prediction aims to predict the quality of apples based on the values contained in the variables of the data set.

Dataset Source:
https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality

This dataset is provided by an American agricultural company with the aim to predict the quality of apples based on certain measurements included in the dataset. 
The dataset contains information about various attributes of the fruit set, such as 
- Size
- Weight
- Sweetness 
- Crunchiness 
- Juiciness 
- Ripeness 
- Acidity
- Quality
The dataset has been scaled and cleaned from scratch from the source dataset for ease of use.

Data processing and modeling are carried out for this apple quality data set so that prediction of apple quality can be done. 
After various stages, the model that has the best performance for this prediction is the Kneighbors Classifier Model with a F1-score macro avg of 0.91 which has previously been tuned, 
then to see if the selected model has run correctly and produces the right output, deploy the model and visualize it on a simple web.app using Streamlit.
