# Requirements

* Python 3.\*
* NumPy \*
* Pandas \*

# Exercise: Practice 3

```
1. Завантажити дані файла Titanic.csv в структуру даних data frame.
2. Перевірити наявність пустих значень в спостереженнях (NaN заначення в
строках).
3. Видалити атрибут, якій містить максимальну кількість відсутніх значень.
4. Видалити спостереження, які містять хоча б одне значення NaN.
5. У окрему структуру даних data frame згрупувати дані спостережнь для
жінок, чоловіків та дітей.
```

# How to run

**1.1**

From the command prompt start `main.py` in the project folder

*This realization has no GUI support so all work will be done in the console*

---

**1.2**

This realization has no user input, so after running you will see the result of the work

**Sample:**
```
Source csv:
      Passenger Class  ... Survived
0              First  ...      Yes
1              First  ...      Yes
2              First  ...       No
3              First  ...       No
4              First  ...       No
...              ...  ...      ...
1304           Third  ...       No
1305           Third  ...       No
1306           Third  ...       No
1307           Third  ...       No
1308           Third  ...       No
[1309 rows x 12 columns]

Number of nans in dataframe:
Passenger Class                          0
Name                                     0
Sex                                      0
Age                                    263
No of Siblings or Spouses on Board       0
No of Parents or Children on Board       0
Ticket Number                            0
Passenger Fare                           1
Cabin                                 1014
Port of Embarkation                      2
Life Boat                              823
Survived                                 0
dtype: int64

Column with max nan: Cabin

Dropped all nans:
      Passenger Class  ... Survived
0              First  ...      Yes
1              First  ...      Yes
5              First  ...      Yes
6              First  ...      Yes
8              First  ...      Yes
...              ...  ...      ...
1026           Third  ...      Yes
1131           Third  ...      Yes
1187           Third  ...      Yes
1188           Third  ...      Yes
1189           Third  ...      Yes
[180 rows x 12 columns]

Dataframe in which deleted column with frequent nan:
      Passenger Class  ... Survived
0              First  ...      Yes
1              First  ...      Yes
2              First  ...       No
3              First  ...       No
4              First  ...       No
...              ...  ...      ...
1304           Third  ...       No
1305           Third  ...       No
1306           Third  ...       No
1307           Third  ...       No
1308           Third  ...       No
[1309 rows x 11 columns]

Grouped by sex and age:
      Passenger Class                                      Name  ... Survived  Child
0              First             Allen, Miss. Elisabeth Walton  ...      Yes  False
377           Second          Collyer, Miss. Marjorie 'Lottie'  ...      Yes   True
1095           Third            O'Sullivan, Miss. Bridget Mary  ...       No  False
923            Third                         Kelly, Miss. Mary  ...      Yes  False
922            Third  Kelly, Miss. Anna Katherine 'Annie Kate'  ...      Yes  False
...              ...                                       ...  ...      ...    ...
571           Second              Troupiansky, Mr. Moses Aaron  ...       No  False
574           Second           Turpin, Mr. William John Robert  ...       No  False
576           Second                           Veal, Mr. James  ...       No  False
552           Second                Rogers, Mr. Reginald Harry  ...       No  False
1308           Third                        Zimmerman, Mr. Leo  ...       No  False
[1309 rows x 12 columns]
```

---