# Cat_dog

### Create an env
1. conda create -n catdog python=3.12 -y 
2. Create an temp.py where our folder dtr will added
3. Create an requirement file and run the dependencies 
touch requirements.txt -> Create the file
pip install -r requirements.txt -> run the file
3. Added the logger file
4. prepare/update the common.py and utility

@staticmethod is a decorator in Python used to define methods inside a class that do not require access to the instance (self) or class (cls). This means that @staticmethod can be called on the class itself without needing to create an instance of the class, and it does not modify or rely on instance-specific data
basically class instance and self not to required to use the function if the fuction have @static method