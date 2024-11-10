## Load Data (First 10 Rows)

### Output
|    |   ID | cancer   | diabetes   | heart_disease   |   EGGSFREQ |   GREENSALADFREQ |   FRIESFREQ |   MILKFREQ |   SODAFREQ |   COFFEEFREQ |   CAKESFREQ |
|---:|-----:|:---------|:-----------|:----------------|-----------:|-----------------:|------------:|-----------:|-----------:|-------------:|------------:|
|  0 | 1003 | Yes      | No         | No              |          7 |                7 |           2 |          1 |          7 |            9 |           1 |
|  1 | 1053 | No       | Yes        | Yes             |          4 |                5 |           5 |          1 |          7 |            8 |           1 |
|  2 | 1006 | Yes      | Yes        | Yes             |          4 |                6 |           6 |          5 |          8 |            9 |           1 |
|  3 | 1166 | No       | No         | No              |          7 |                3 |           2 |          2 |          1 |            1 |           7 |
|  4 | 1134 | Yes      | No         | No              |          5 |                6 |           3 |          1 |          3 |            9 |           1 |
|  5 | 1014 | No       | No         | No              |          3 |                6 |           5 |          1 |          1 |            8 |           2 |
|  6 | 1074 | Yes      | No         | No              |          4 |                3 |           2 |          1 |          5 |            9 |           3 |
|  7 | 1151 | Yes      | No         | Yes             |          7 |                4 |           3 |          3 |          2 |            1 |           3 |
|  8 | 1001 | Yes      | Yes        | Yes             |          4 |                4 |           5 |          1 |          1 |            9 |           1 |
|  9 | 1048 | Yes      | No         | No              |          5 |                3 |           2 |          1 |          1 |            9 |           2 |

## SQL Query Results

### Query
```sql
SELECT 
        ID, 
        SODAFREQ, 
        EGGSFREQ, 
        FRIESFREQ 
    FROM Nutrition 
    WHERE SODAFREQ > 3 
    ORDER BY SODAFREQ DESC 
    LIMIT 5
```

### Output
|    |   ID |   SODAFREQ |   EGGSFREQ |   FRIESFREQ |
|---:|-----:|-----------:|-----------:|------------:|
|  0 | 1138 |          9 |          1 |           3 |
|  1 | 1071 |          9 |          2 |           5 |
|  2 | 1034 |          9 |          5 |           4 |
|  3 | 1054 |          9 |          4 |           4 |
|  4 | 1006 |          8 |          4 |           6 |

## SQL Query Results

### Query
```sql
SELECT 
        AVG(EGGSFREQ) as avg_eggs,
        AVG(GREENSALADFREQ) as avg_salad,
        AVG(FRIESFREQ) as avg_fries,
        AVG(MILKFREQ) as avg_milk,
        AVG(SODAFREQ) as avg_soda,
        AVG(COFFEEFREQ) as avg_coffee,
        AVG(CAKESFREQ) as avg_cakes
    FROM Nutrition
```

### Output
|    |   avg_eggs |   avg_salad |   avg_fries |   avg_milk |   avg_soda |   avg_coffee |   avg_cakes |
|---:|-----------:|------------:|------------:|-----------:|-----------:|-------------:|------------:|
|  0 |    4.77778 |     5.22222 |     4.03704 |    2.75926 |    4.12963 |      5.88889 |     2.16667 |

## Data Transformation (First 20 Rows)

### Output
|    |   ID |   healthy_total |   unhealthy_total | has_health_condition   |
|---:|-----:|----------------:|------------------:|:-----------------------|
|  0 | 1003 |              24 |                10 | True                   |
|  1 | 1053 |              18 |                13 | True                   |
|  2 | 1006 |              24 |                15 | True                   |
|  3 | 1166 |              13 |                10 | False                  |
|  4 | 1134 |              21 |                 7 | True                   |
|  5 | 1014 |              18 |                 8 | False                  |
|  6 | 1074 |              17 |                10 | True                   |
|  7 | 1151 |              15 |                 8 | True                   |
|  8 | 1001 |              18 |                 7 | True                   |
|  9 | 1048 |              18 |                 5 | True                   |
| 10 | 1073 |              20 |                15 | True                   |
| 11 | 1075 |              17 |                 4 | True                   |
| 12 | 1051 |              17 |                12 | True                   |
| 13 | 1173 |              15 |                 8 | True                   |
| 14 | 1148 |              15 |                 8 | False                  |
| 15 | 1105 |              24 |                10 | True                   |
| 16 | 1008 |              26 |                12 | False                  |
| 17 | 1192 |              18 |                 6 | True                   |
| 18 | 1081 |               7 |                 3 | True                   |
| 19 | 1103 |              21 |                11 | False                  |

## SQL Query Results

### Query
```sql
SELECT 
        ID, 
        SODAFREQ, 
        EGGSFREQ, 
        FRIESFREQ 
    FROM Nutrition 
    WHERE SODAFREQ > 3 
    ORDER BY SODAFREQ DESC 
    LIMIT 5
```

### Output
|    |   ID |   SODAFREQ |   EGGSFREQ |   FRIESFREQ |
|---:|-----:|-----------:|-----------:|------------:|
|  0 | 1138 |          9 |          1 |           3 |
|  1 | 1071 |          9 |          2 |           5 |
|  2 | 1034 |          9 |          5 |           4 |
|  3 | 1054 |          9 |          4 |           4 |
|  4 | 1006 |          8 |          4 |           6 |

## SQL Query Results

### Query
```sql
SELECT 
        AVG(EGGSFREQ) as avg_eggs,
        AVG(GREENSALADFREQ) as avg_salad,
        AVG(FRIESFREQ) as avg_fries,
        AVG(MILKFREQ) as avg_milk,
        AVG(SODAFREQ) as avg_soda,
        AVG(COFFEEFREQ) as avg_coffee,
        AVG(CAKESFREQ) as avg_cakes
    FROM Nutrition
```

### Output
|    |   avg_eggs |   avg_salad |   avg_fries |   avg_milk |   avg_soda |   avg_coffee |   avg_cakes |
|---:|-----------:|------------:|------------:|-----------:|-----------:|-------------:|------------:|
|  0 |    4.77778 |     5.22222 |     4.03704 |    2.75926 |    4.12963 |      5.88889 |     2.16667 |

## Data Transformation (First 20 Rows)

### Output
|    |   ID |   healthy_total |   unhealthy_total | has_health_condition   |
|---:|-----:|----------------:|------------------:|:-----------------------|
|  0 | 1003 |              24 |                10 | True                   |
|  1 | 1053 |              18 |                13 | True                   |
|  2 | 1006 |              24 |                15 | True                   |
|  3 | 1166 |              13 |                10 | False                  |
|  4 | 1134 |              21 |                 7 | True                   |
|  5 | 1014 |              18 |                 8 | False                  |
|  6 | 1074 |              17 |                10 | True                   |
|  7 | 1151 |              15 |                 8 | True                   |
|  8 | 1001 |              18 |                 7 | True                   |
|  9 | 1048 |              18 |                 5 | True                   |
| 10 | 1073 |              20 |                15 | True                   |
| 11 | 1075 |              17 |                 4 | True                   |
| 12 | 1051 |              17 |                12 | True                   |
| 13 | 1173 |              15 |                 8 | True                   |
| 14 | 1148 |              15 |                 8 | False                  |
| 15 | 1105 |              24 |                10 | True                   |
| 16 | 1008 |              26 |                12 | False                  |
| 17 | 1192 |              18 |                 6 | True                   |
| 18 | 1081 |               7 |                 3 | True                   |
| 19 | 1103 |              21 |                11 | False                  |

## SQL Query Results

### Query
```sql
SELECT 
        ID, 
        SODAFREQ, 
        EGGSFREQ, 
        FRIESFREQ 
    FROM Nutrition 
    WHERE SODAFREQ > 3 
    ORDER BY SODAFREQ DESC 
    LIMIT 5
```

### Output
|    |   ID |   SODAFREQ |   EGGSFREQ |   FRIESFREQ |
|---:|-----:|-----------:|-----------:|------------:|
|  0 | 1138 |          9 |          1 |           3 |
|  1 | 1071 |          9 |          2 |           5 |
|  2 | 1034 |          9 |          5 |           4 |
|  3 | 1054 |          9 |          4 |           4 |
|  4 | 1006 |          8 |          4 |           6 |

## SQL Query Results

### Query
```sql
SELECT 
        AVG(EGGSFREQ) as avg_eggs,
        AVG(GREENSALADFREQ) as avg_salad,
        AVG(FRIESFREQ) as avg_fries,
        AVG(MILKFREQ) as avg_milk,
        AVG(SODAFREQ) as avg_soda,
        AVG(COFFEEFREQ) as avg_coffee,
        AVG(CAKESFREQ) as avg_cakes
    FROM Nutrition
```

### Output
|    |   avg_eggs |   avg_salad |   avg_fries |   avg_milk |   avg_soda |   avg_coffee |   avg_cakes |
|---:|-----------:|------------:|------------:|-----------:|-----------:|-------------:|------------:|
|  0 |    4.77778 |     5.22222 |     4.03704 |    2.75926 |    4.12963 |      5.88889 |     2.16667 |

## Data Transformation (First 20 Rows)

### Output
|    |   ID |   healthy_total |   unhealthy_total | has_health_condition   |
|---:|-----:|----------------:|------------------:|:-----------------------|
|  0 | 1003 |              24 |                10 | True                   |
|  1 | 1053 |              18 |                13 | True                   |
|  2 | 1006 |              24 |                15 | True                   |
|  3 | 1166 |              13 |                10 | False                  |
|  4 | 1134 |              21 |                 7 | True                   |
|  5 | 1014 |              18 |                 8 | False                  |
|  6 | 1074 |              17 |                10 | True                   |
|  7 | 1151 |              15 |                 8 | True                   |
|  8 | 1001 |              18 |                 7 | True                   |
|  9 | 1048 |              18 |                 5 | True                   |
| 10 | 1073 |              20 |                15 | True                   |
| 11 | 1075 |              17 |                 4 | True                   |
| 12 | 1051 |              17 |                12 | True                   |
| 13 | 1173 |              15 |                 8 | True                   |
| 14 | 1148 |              15 |                 8 | False                  |
| 15 | 1105 |              24 |                10 | True                   |
| 16 | 1008 |              26 |                12 | False                  |
| 17 | 1192 |              18 |                 6 | True                   |
| 18 | 1081 |               7 |                 3 | True                   |
| 19 | 1103 |              21 |                11 | False                  |

