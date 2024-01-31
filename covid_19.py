import pandas as pd
import matplotlib.pyplot as plt

def menu():
    print()
    print("***********************************************************")
    print("                  Covid 19 in INDIA ")
    print("***********************************************************")
    print()
    print('    0. Know about the Project')
    print('Working with Covid 19 in INDIA file')
    print('    1. Reading file Covid 19 in INDIA')
    print('    2. Reading file Covid 19 in INDIA without Index')
    print('    3. Assign new Column names')
    print('Data Manipulation')
    print('    4. Display specific column')
    print('    5. Read 6 records from file - Covid 19 in INDIA')
    print('    6. Read 3 records from top and2 from bottom from file - emp')
    print('    7. Arrange in Ascending Order by State/UnionTerritory')
    print('    8. Max no. of Deaths')
    print('    9. Min no. of Deaths')
    print('Data Visualisation')
    print('   10. Line Chart')
    print('   11. Bar Chart')
    print('   12. Pie Chart')
    print('   13. Barh chart')
    print('Working with State wise Sample Report')
    print('   14.Reading State Wise Samples')
    print('   15.Show Total no. of Negative Samples')
    print('   16. Pie Plot for Positive and Negative Samples')
    print()
    print()

    print('*********************************************************')

    
menu()

def about():
    print('In this Project Data Analysis is done on Covid 19 in INDIA')

def csv():
    print('Reading file Covid 19 in INDIA')
    print()
    print()
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df)

def no_index():
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv',index_col=0)
    print('without index')
    print()
    print(df)
    print()


def new_column():
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv',skiprows=1)
    print(df)


def read_rows():
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv',nrows=6)
    print('Show 6 Records')
    print(df)


def top_bottom():
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print('Top 3 rows')
    print(df.head(3))
    print()
    print()
    print('Last 2 rows')
    print(df.tail(2))

def sort_state():
    print('sorting Members names in Ascending order')
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv',index_col=0)
    df=df.sort_values('10 States')
    print(df)

def maxdeaths():
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df)
    print('Highest Deaths')
    print(df.Deaths.max())

def mindeaths():
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df)
    print('Lowest Deaths')
    print(df.Deaths.min())

def line_chart():
    print('Line Chart')
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df)
    plt.title('Covid 19 records')
    plt.plot()
    plt.show()

def bar_chart():
    print('Bar Chart')
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df)
    x=df['Cured']
    y=df['Deaths']
    plt.title('Deaths and Cured Data in INDIA')
    plt.xlabel('Deaths')
    plt.ylabel('Cured')
    plt.bar(x,y,color='red')
    plt.show()

def pie_chart():
    print('Pie Chart')
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df)
    plt.title(' Cases in a State or Union Territory')
    z=eval(input('Enter Values of Statein sq brackets:'))
    color=['white','orange','purple']
    items=['Cured','Death','Confirmed']
    expl=[0,0,0.2]
    plt.pie(z,colors=color,label=items,explode=expl,autopct='%5.1f%%')
    plt.show()

def barh_chart():
    print('Barh Chart')
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df)
    x=df['Cured']
    y=df['State/UnionTerritory']
    plt.title('Cured in Various States and UT')
    plt.xlabel('Deaths')
    plt.ylabel('Cured')
    plt.barh(x,y,color='red')
    plt.show()

def statewisesample():
    print('Reading File State Wise Sample Report')
    print()
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df)

def totalnegative():
    print('Total Negative Cases')
    print()
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df['Negative'].count())

def pie_plot():
    df=pd.read_csv('C:\\Users\\ADITYA\\OneDrive\\Desktop\\VIT-BHOPAL\\Python\\COVID 19 Project.csv')
    print(df)
    plt.title(' Positive and Negative Caese in a State or Union Territory')
    z=eval(input('EnterValues of a State in sq brackets:'))
    color=['blue','yellow','purple']
    items=['TotalSamples','Negative','Positive']
    expl=[0,0,0.4]
    plt.plot(z,colors=color,label=items,explode=expl,autopct='%5.1f%%')
    plt.show()






opt=''
opt=int(input('Enter your choice:'))
if opt==0:
    about()
if opt==1:
    csv()
if opt==2:
    no_index()
elif opt==3:
    new_colomn()
elif opt==4:
    spec_col()
elif opt==5:
    read_rows()
elif opt==6:
    top_bottom()
elif opt==7:
    sort_state()
elif opt==8:
    maxdeaths()
elif opt==9:
    mindeaths()
elif opt==10:
    line_chart()
elif opt==11:
    bar_chart()
elif opt==12:
    pie_chart()
elif opt==13:
    barh_chart()
elif opt==14:
    statewisesample()
elif opt==15:
    totalnegative()
elif opt==16:
    pie_plot()
else:
    print('INVALID OPTION')
    print('\a')
