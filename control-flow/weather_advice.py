#Ask the user to input the current weather from a predefined set of conditions: 
current_weather= input("What's the weather like today? (sunny/rainy/cold): ") .lower() 
#Provide Clothing Recommendations:
#If the weather is “sunny”, recommend.
if current_weather == "sunny":
    print ("Wear a t-shirt and sunglasses.")
elif current_weather == "rainy":
    print ("Don't forget your umbrella and a raincoat.")
elif current_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")