import requests  
from bs4 import BeautifulSoup  # מייבא את מודול Beautiful Soup 4.


city = input("Enter city name: ")

# מייצר מחרוזת שמכילה את שם העיר שהמשתמש הזין .
search = "  the wea {}".format(city)

headers = {
    "Accept-Language": "en-US,en;q=0.5"
}


# מייצר URL לחיפוש ב-Google 
# באמצעות המחרוזת שנוצרה בשלב הקודם.
# ה-URL מיועד לחיפוש אחר מידע מזג האוויר בעיר שהמשתמש הזין.
url = "https://www.google.com/search?q={}".format(search)

# שולח בקשת GET ל-URL
# שנוצר בשלב הקודם ומקבל תשובה מהשרת. התשובה מכילה את התוכן
# של הדף האינטרנט שבו מוצג מידע מזג האוויר.
response = requests.get(url)

# משתמש ב-BeautifulSoup 
# כדי לפרק את התוכן שנמצא בתשובה מהשרת. המודול יבצע את הפירוק
# ויהפוך את התוכן למבנה שנוח לעבוד איתו.
# הפרסום עובר באמצעות HTML.parser שמאפשר לנו לנווט במבנה HTML.
soup = BeautifulSoup(response.text, "html.parser")

# משתמש ב-BeautifulSoup 
# כדי למצוא את האלמנט div שמכיל מידע מזג האוויר.
# המידע הזה מופיע ב-HTML  
# נמצא ב-class בשם "BNeawe".
# הפעולה soup.find 
# מחפשת את האלמנט הראשון שמתאים לקריטריונים שמועברים אליה ומחזירה את התוכן שבו 
weather = soup.find("div", class_="BNeawe").text

# בודק אם לא נמצא מידע מזג האוויר (אם המשתנה weather הוא None).
if weather is None:
    print("No weather found")
    exit()  # אם לא נמצא מידע, יוצא מהתוכנית.

# אם נמצא מידע , מדפיס את המידע שנמצא.
print(weather)
