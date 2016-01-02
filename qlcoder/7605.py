import json
data = {'name':'Sayalic' , 'age':'25' , 'girlfriend':None ,
        'gayfriend':{
            'age':'24.5',
            'name':'dploop',
            'FavoriteFruits':['pear' , 'lemon']
        },
        'FavoriteFruits':['orange' , 'banana' , 'apple']
        }

print(json.dumps(data))