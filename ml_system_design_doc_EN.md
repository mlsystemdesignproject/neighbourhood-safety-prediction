# ML System Design Doc - Neighbourhood Safety Prediction [EN]
## ML System Design - Predicting Safety Levels in London Boroughs

### 1. Objectives
#### 1.1. Justification of Product Development

##### Business Goal
The business goal is to develop an ML model that accurately predicts safety levels in London neighbourhoods for the next 6 months. The predictions will be used for:
- decision-making on safety management in London Boroughs
- awareness of residents about the safety levels in specific Boroughs

##### Secondary Business Goal
The secondary business goal is to improve safety in London neighbourhoods through more efficient resource allocation and information available to residents.

##### Current Business Process Description
Currently, the historical  safety level in London can be assessed from various sources, including:
- police reports
- crime data

##### Benefits of Implementing the ML Model
The introduction of the ML model will allow us to predict the level of safety in London Boroughs. This will contribute to improving the efficiency of safety management and improve the level of security in general.

##### Success Criteria for the ML Model:
- Prediction accuracy should be ..... *(DS)*
- Predictions should be useful for making safety management decisions.

#### 1.2. Business Requirements and Constraints

##### Vision
- Predictions of safety levels for the next 6 *(??? team meeting @Sun)* months are required. Predictions are obtained once a month until the end of the month.
- Granularity of calculation: Individual Boroughs, crimes per month
- Breakdown by various types of crimes *(how many?)* categories
- Historical data is loaded *(how often?) *
- Creating a dashboard for model predictions visualisation *(requirements?) *

##### Business Requirements and Constraints for the Pilot
- It is necessary to make safety level predictions for the next 6 months by the end of December.
- Granularity of calculation: Individual Boroughs, crimes per month
- Only certain types of crime are predicted *(how many categories?) *

##### Pilot Execution
- Model testing and pilot evaluation will be conducted on open data from the London Metropolitan Police and aggregated *(???) * data on social events in London.

#### 1.3. What is included in the Iteration Scope and what is not
*(DS)*

#### 1.4. Tools
*(DS)*
- The project is being conducted in GitHub
- Documentation is on Google Docs on Google Drive *(??? DS)*. It should contain algorithm descriptions and intermediate test results *(??? DS)*
- Code is in JupyterLab, corresponds to PEP8, and divided into modules (??? DS)
- Stack: *(? Where?? DS)*
- Database: *(? Which one?? DS)*

#### 2. Methodology
[Here should be a description of the methodology used for ML model development. You can mention data preprocessing methods, model selection, training, and evaluation. - *(DS)*]

#### 3. Project Implementation Costs
Implementation costs include expenses for model development and deploying the model into operation.

#### *(??? Which point?) * ML System Design
ML model will be built using regression *(??? DS)* model. Data from the following sources will be used as input data for the model:
- Crime data
- Data on social events in the area
- Weather data *(???) *

#### Conclusions
Developing an ML model for predicting safety levels in London neighbourhoods is a promising direction. Model implementation will allow more accurate safety predictions, contributing to increased safety management efficiency and overall safety improvement.

#### Additional Recommendations
The following additional information can be included in the document:
- A detailed description of the regression model that will be used for safety level prediction.
- Data collection plan for the ML model.
- Model deployment plan.
- Evaluation of the economic efficiency of this model.