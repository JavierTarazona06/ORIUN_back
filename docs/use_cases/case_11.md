# Endpoints for Case 11

## 1. Get statistics

**URL:** `call/statistics/`

**Method:** `GET`

**Description:** Used get info about historical data of the calls. In order to do that, it takes one parameter about the students and another about the calls, and returns the data.

**Authorization:** None, it is public

**Inputs:** query params 

| Name           | Type   | Description                                                                                                                                                                                  |
|----------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `data_student` | String | Parameter from the students to use for the analysis. The possible values are: `faculty`, `major`, `sex`, `admission`, `study_level`, `ethnicity`, `headquarter`, `PBM`, `PAPA` or `advance`. |
| `data_call`    | String | Parameter from the calls to use for the analysis. The possible values are: `university`, `country`, `region` or `semester`.                                                                  |

**Outputs:**

In the returned JSON there is a key called `type_chart`. It indicates whether the chart must be a `table` or a `candle` (candle sticks). For each type of chart the output is different. 

For table:

| Name         | Type                 | Description                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `postulates` | List of dictionaries | It contains a count of the students that fell into each category. Each dictionary in the list is each row of the table, so it contains the category of the row and its name (for example `"university": "Universidad de los Andes"`) and the number of students for each `data_student` selected (for example if the category selected was sex then it would be `"Masculino": 1, "Femenino": 3` . |
| `winners`    | List of dictionaries | Same as the previous one but it indicates the actual winners of the calls.                                                                                                                                                                                                                                                                                                                        |

For candle:

| Name         | Type                 | Description                                                                                                                                                                                                                                                                                                                                                 |
|--------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `postulates` | List of dictionaries | It contains a count of the students that fell into each category. Each dictionary contains 3 values, one is the category of the call selected, such as university, and the other two are the minimum and maximum value for the category selected for the students. For example it could be `"university": "Universidad de los Andes", "min": 2, "max": 50`. |
| `winners`    | List of dictionaries | Same as the previous one but it indicates the actual winners of the calls.                                                                                                                                                                                                                                                                                  |