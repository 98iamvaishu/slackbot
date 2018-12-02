from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slackclient import SlackClient
from events.models import Text
import random
import re

SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,                          #2
'SLACK_BOT_USER_TOKEN', None)                                     #
Client = SlackClient(SLACK_BOT_USER_TOKEN)                        #3

class Events(APIView):
	def post(self, request, *args, **kwargs):

		slack_message = request.data

		if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
			return Response(status=status.HTTP_403_FORBIDDEN)

		# verification challenge
		if slack_message.get('type') == 'url_verification':
			return Response(data=slack_message,
							status=status.HTTP_200_OK)
		# greet bot
		if 'event' in slack_message:                              #4
			event_message = slack_message.get('event')            #
			
			# ignore bot's own message
			if event_message.get('subtype') == 'bot_message':     #5
				return Response(status=status.HTTP_200_OK)        #
			
			# process user's message
			user = event_message.get('user')                      #6
			text = event_message.get('text')      
			msg1 = Text(msg=text)
			msg1.save()                #
			channel = event_message.get('channel')  
			intro = ['hi','hii','hiii','hello','hola'] 
			reply = random.choice(['hey','hola','sup','ola'])             #
			bot_text = '{} <@{}>:wave:'.format(reply,user)    
			for i in intro:         #
				if i == text.lower():                              #7
					Client.api_call(method='chat.postMessage',        #8
								channel=channel,                  #
								text=bot_text)                    #
					return Response(status=status.HTTP_200_OK)   
					break

			# if text.lower() == 'send' :      
			get = Text.objects.all()
			print(get)
			happy = [':sunglasses:',':grin:',':grinning:',':smiley:',':smile:']
			sad = [':disappointed_relieved:',':pensive:',':white_frowning_face:',':disappointed:']
			anger = [':rage:',':angry:',':imp:']
			a =[]
			sq = "Its always seem impossible until it's done"
			hq = "Cherish all your happy moments; they make a fine cushion for old age."
			aq = "Think of all the beauty still left around you and be happy"
			for i in get:
				a.append(i.msg.split(" "))
			print(a)
			# if text =="How are you":
			# 	Client.api_call(method='chat.postMessage',        #8
			# 						channel=channel,                  #
			# 						text="")                   #
			# 	return Response(status=status.HTTP_200_OK) 
			if text in happy:
				Client.api_call(method='chat.postMessage',        #8
									channel=channel,                  #
									text=hq)                   #
				return Response(status=status.HTTP_200_OK) 
			elif text in sad:
				Client.api_call(method='chat.postMessage',        #8
									channel=channel,                  #
									text=sq)                  #
				return Response(status=status.HTTP_200_OK)
			elif text in anger:
				Client.api_call(method='chat.postMessage',        #8
									channel=channel,                  #
									text=aq)        #
				return Response(status=status.HTTP_200_OK)
			else:
				Client.api_call(method='chat.postMessage',        #8
									channel=channel,                  #
									text="Life is beautiful just enjoy whatever you have")        #
				return Response(status=status.HTTP_200_OK)


							
				# for j in a:
				#     if x in happy:
				#         Client.api_call(method='chat.postMessage',        #8
				#                     channel=channel,                  #
				#                     text=hq)        
				#         print(1)            #
				#         return Response(status=status.HTTP_200_OK) 

				#         break
				#     elif y in sad:
				#         Client.api_call(method='chat.postMessage',        #8
				#                     channel=channel,                  #
				#                     text=sq)
				#         print(2)                    #
				#         return Response(status=status.HTTP_200_OK) 
				#         break
				#     elif z in anger:
				#         Client.api_call(method='chat.postMessage',        #8
				#                     channel=channel,                  #
				#                     text=aq)                    #
				#         return Response(status=status.HTTP_200_OK) 
				#         break
				#     else :
				#         pass











			# return Response(status=status.HTTP_200_OK)