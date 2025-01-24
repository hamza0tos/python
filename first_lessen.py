# ========================== Variables ==========================
# تعريف المتغيرات (Variables):
# متغير يستخدم لتخزين البيانات التي يمكن إعادة استخدامها أو تغييرها لاحقًا.

name = "hamza"  # سلسلة نصية (String)
age = 16         # رقم صحيح (Integer)
is_alive = True  # قيمة منطقية (Boolean)

# ========================== Conditions ==========================
# الجمل الشرطية (if, elif, else):
# تُستخدم لاتخاذ قرارات بناءً على شروط معينة.

age = 18
if age < 18:  # إذا كان العمر أقل من 18
    print("You are minor")  # طباعة "أنت قاصر"
elif age == 18:  # إذا كان العمر يساوي 18
    print("You are 18!")
else:  # في أي حالة أخرى (العمر أكبر من 18)
    print("You are adult.")

# ========================== Loops ==========================
# الحلقات (Loops):
# تُستخدم لتكرار كود معين عددًا محددًا من المرات أو حتى يتحقق شرط معين.

# ---- For Loop ----
# تُستخدم لتكرار كود لعدد محدد من المرات أو على عناصر في تسلسل (مثل قائمة).
for i in range(5):  # تكرار الكود 5 مرات (من 0 إلى 4)
    print(i)

# ---- While Loop ----
# تُستخدم لتكرار كود حتى يتحقق شرط معين.
counter = 0
while counter < 5:  # طالما العداد أقل من 5
    print("Counter:", counter)
    counter += 1  # زيادة العداد بمقدار 1 في كل تكرار

# ========================== Lists ==========================
# القوائم (Lists):
# تُستخدم لتخزين مجموعة من العناصر القابلة للتغيير (Mutable) مرتبة (Ordered).

fruits = ["apple", "orange", "watermelon"]  # قائمة بالفواكه
fruits.append(input("Add a fruit: "))  # إضافة عنصر جديد إلى القائمة
print(fruits[0])  # طباعة أول عنصر في القائمة (apple)

# ========================== OOP (Object-Oriented Programming) ==========================
# البرمجة الكائنية (OOP):
# تعتمد على إنشاء كائنات (Objects) باستخدام الفئات (Classes).

class Car:  # تعريف فئة سيارة
    def __init__(self, brand, model):  # مُنشئ الفئة (Constructor)
        self.brand = brand  # خاصية العلامة التجارية
        self.model = model  # خاصية الطراز

    def display_info(self):  # دالة لعرض المعلومات
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla")  # إنشاء كائن جديد من الفئة Car
car1.display_info()  # استدعاء الدالة لعرض معلومات السيارة

# ========================== Files ==========================
# التعامل مع الملفات (File Handling):
# يُمكنك قراءة وكتابة بيانات من/إلى ملف.

# ---- كتابة إلى ملف ----
with open("filename.txt", "w") as file:  # فتح ملف في وضع الكتابة (Write)
    file.write("Hello, world!")  # كتابة النص إلى الملف

# ---- قراءة من ملف ----
with open("filename.txt", "r") as file:  # فتح ملف في وضع القراءة (Read)
    content = file.read()  # قراءة محتويات الملف
    print(content)

# ========================== Functions ==========================
# الدوال (Functions):
# تُستخدم لتجميع الكود القابل لإعادة الاستخدام.

def greet(name):  # تعريف دالة تُرحب باسم معين
    return f"Hello, {name}"  # إرجاع النص

message = greet("hamza")  # استدعاء الدالة
print(message)  # طباعة الرسالة

# ========================== Advanced Concepts ==========================
# المفاهيم المتقدمة:

# ---- Dictionary ----
# القواميس (Dictionaries): تخزن البيانات كأزواج مفتاح وقيمة.
info = {"name": "Hamza", "age": 16, "is_alive": True}
print(info["name"])  # طباعة قيمة المفتاح "name"

# ---- Try and Except ----
# تُستخدم للتعامل مع الأخطاء أثناء تشغيل البرنامج.
try:
    number = int(input("Enter a number: "))  # محاولة تحويل المدخل إلى رقم
    print(f"You entered: {number}")
except ValueError:  # التعامل مع خطأ الإدخال إذا لم يكن رقمًا
    print("Invalid input! Please enter a number.")

# ---- Lambda Functions ----
# دوال Lambda: تُستخدم لإنشاء دالة صغيرة ومختصرة.
square = lambda x: x ** 2  # دالة Lambda تُرجع مربع الرقم
print(square(5))  # النتيجة: 25

# ---- List Comprehension ----
# اختصارات القوائم: طريقة مختصرة لإنشاء قوائم.
numbers = [x for x in range(10) if x % 2 == 0]  # إنشاء قائمة بالأعداد الزوجية من 0 إلى 9
print(numbers)  # النتيجة: [0, 2, 4, 6, 8]

# ---- Inheritance (OOP) ----
# الوراثة: تُستخدم لإنشاء فئات جديدة بناءً على فئات موجودة.
class ElectricCar(Car):  # فئة ElectricCar ترث من الفئة Car
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # استدعاء مُنشئ الفئة الأصلية
        self.battery_size = battery_size  # خاصية جديدة

    def display_info(self):
        super().display_info()  # استدعاء الدالة الأصلية
        print(f"Battery Size: {self.battery_size} kWh")

e_car = ElectricCar("Tesla", "Model S", 100)
e_car.display_info()

# ========================== End of Guide ==========================
# هذا الكود يغطي معظم أساسيات ومتقدمات Python مع شرح لكل جزء.
