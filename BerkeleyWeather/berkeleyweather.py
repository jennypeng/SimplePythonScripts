import urllib2
import json
f = urllib2.urlopen('http://api.wunderground.com/api/6fca8cfade0939b0/conditions/q/CA/Berkeley.json')
g = urllib2.urlopen('http://api.wunderground.com/api/6fca8cfade0939b0/forecast/q/CA/Berkeley.json')
h = urllib2.urlopen('http://api.wunderground.com/api/6fca8cfade0939b0/hourly/q/CA/San_Francisco.json')
conditions_json_string = f.read()
hourly_json_string = h.read()
forecast_json_string = g.read()
forecast_parsed_json = json.loads(forecast_json_string)
hourly_parsed_json = json.loads(hourly_json_string)
conditions_parsed_json = json.loads(conditions_json_string)
current_temp = conditions_parsed_json['current_observation']['temperature_string']
feels_like_temp = conditions_parsed_json['current_observation']['feelslike_string']
feelslike_int = float(conditions_parsed_json['current_observation']['feelslike_f'])
current_icon_string = forecast_parsed_json['forecast']['txt_forecast']['forecastday'][0]['icon']
current_day = forecast_parsed_json['forecast']['txt_forecast']['forecastday'][0]['title']
tomorrowdict={"Wednesday":"Thursday", "Thursday":"Friday", "Friday":"Saturday", "Saturday":"Sunday", "Sunday":"Monday", "Monday":"Tuesday", "Tuesday":"Wednesday"}
# def convert_time_to_int(time):
# 	timedict={"1 AM":1,"2 AM":2, "3 AM":3, "4 AM": 4, "5 AM":5, "6 AM": 6, "7 AM":7, "8 AM":8, "9 AM":9, "10 AM": 10, "11 AM": 11, "12 PM": 12, "1 PM": 13, "2 PM": 14, "3 PM":15, "4 PM":16, "5 PM":17, "6 PM":18, "7 PM":19,
# 	"8 PM":20, "9 PM":21, "10 PM":22, "11 PM":23, "12 AM":0}
# 	return timedict[time]
def prompt():
	print "Hi! Welcome to Berkeley Weather."
	go_out_time = raw_input("When are you planning on going out? Now? Later today? Tomorrow? Never?" + "\n")
	
	if "Now" in go_out_time or "now" in go_out_time:
		if feelslike_int>90:
			print "Current temperature in Berkeley is %s, but it feels like %s. You can wear shorts, a tanktop, or a dress!" % (current_temp,feels_like_temp)
		elif feelslike_int>80:
			print "Current temperature in Berkeley is %s, but it feels like %s. You can wear shorts with a thin shirt!" % (current_temp,feels_like_temp)
		elif feelslike_int>70:
			print "Current temperature in Berkeley is %s, but it feels like %s. You can wear a lightweight shirt with jeans!" % (current_temp,feels_like_temp)
		elif feelslike_int>60:
			print "Current temperature in Berkeley is %s, but it feels like %s. You can wear jeans and a long-sleeve. Make sure to bring a sweater or you might get cold!" % (current_temp,feels_like_temp)
		elif feelslike_int>50:
			print "Current temperature in Berkeley is %s, but it feels like %s. You can wear jeans and a jacket. Make sure to layer!" % (current_temp,feels_like_temp)
		elif feelslike_int>40:
			print "It's getting cold! Current temperature in Berkeley is %s, but it feels like %s. Wear some long socks, a hat, and a thick jacket. Don't forget to put on a pair of pants and a scarf!" % (current_temp,feels_like_temp)
		elif feelslike_int>30:
			print "It's getting cold! Current temperature in Berkeley is %s, but it feels like %s. Wear some long socks, a hat, thick jacket and gloves. Don't forget to put on a pair of pants and a scarf!" % (current_temp,feels_like_temp)
		elif feelslike_int<30:
			print "Are you sure you want to go outside? Current temperature in Berkeley is %s, but it feels like %s. " % (current_temp,feels_like_temp)
		if current_icon_string == "chanceofrain":
			print "There's a chance of rain! Think about bringing an umbrella!"
	
	elif "Later" in go_out_time or "later" in go_out_time:
		
		timeout = raw_input("About what time are you planning on going out? _:00 PM/AM" + "\n")
		# inttime=convert_time_to_int(timeout)
		return later_today(current_day, timeout)
	
	elif "Never" in go_out_time or "never" in go_out_time:
		print "You should go outside at least once every two days for fresh air and friends!"
		return prompt()
	elif "tomorrow" in go_out_time or "Tomorrow" in go_out_time:
		timeouttomorrow = raw_input("About what time tomorrow are you planning on going out? _:00 PM/AM" + "\n")
		return later_today(tomorrowdict[current_day], timeouttomorrow)
	else:
		print "Opps! I couldn't understand you!"
		return prompt()

def later_today(day, time):
	lst=[]
	hour=hourly_parsed_json["hourly_forecast"]
	for item in hour:
		if type(item)==dict:
			foo=item["FCTTIME"]
			keys=foo.keys()
       		values=foo.values()
        	if day and time in values:
        		lst.append(item["condition"])  
        		lst.append(item["temp"]["english"])
    	a=int(lst[1])
    	b=str(lst[0])
    	return what_to_wear(a,b)
def what_to_wear(temperature,condition):
		if temperature>90:
			print "It'll be around %s F in Berkeley. You can wear shorts, a tanktop, or a dress!" % (temperature)
		elif temperature>80:
			print "It'll be around %s F in Berkeley. You can wear shorts with a thin shirt!" % (temperature)
		elif temperature>70:
			print "It'll be around %s F in Berkeley. You can wear a lightweight shirt with jeans!" % (temperature)
		elif temperature>60:
			print "It'll be around %s F in Berkeley. You can wear jeans and a long-sleeve. Make sure to bring a sweater or you might get cold!" % (temperature)
		elif temperature>50:
			print "It'll be around %s F in Berkeley. You can wear jeans and a jacket. Make sure to layer!" % (temperature)
		elif temperature>40:
			print "It's getting cold! It'll be around %s F in Berkeley. Wear some long socks, a hat, and a thick jacket. Don't forget to put on a pair of pants and a scarf!" % (temperature)
		elif temperature>30:
			print "It's getting cold! It'll be around %s F in Berkeley. Wear some long socks, a hat, thick jacket and gloves. Don't forget to put on a pair of pants and a scarf!" % (temperature)
		elif temperature<30:
			print "Are you sure you want to go outside? It'll be around %s F in Berkeley!!! " % (temperature)
		if condition == "chanceofrain":
			print "There's a chance of rain! Think about bringing an umbrella!"
		return prompt()
prompt()




