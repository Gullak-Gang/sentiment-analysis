from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from typing import List
from caption_generator import get_captions
from dotenv import load_dotenv
import os
import re
import json

load_dotenv()

# Access the API key and model
groq_api_key = os.getenv('groq_api_key')
model = os.getenv('model')
if not groq_api_key:
    raise ValueError("API_KEY not found")

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fetch data from an external API (e.g., Twitter, Instagram)
@app.post("/get_data")  # TEST endpoint
async def get_data(): 
    data = [
    "If you love our cute kinis from ESSENTIAL SOLIDS 💗 this is the opportunity to get it for only $20 at BLACK FRIDAY 🥂⁣\n\n#blackfriday #blackfridaydeals #bikinisale #deals #paia",
    "Black Friday Weekend: Share the Gift of Wellness\n\nIndulge in relaxation and self-care this holiday season. Gift a massage or facial to your loved ones and inspire them to prioritize their well-being.🎁🌿\n\n🔗 https://www.handandstonelakeoswego.com/\n\n#BlackFriday #GiftOfWellness #HandAndStone #SelfCare #HolidayGifts",
    "It’s Black Friday and this year we’re doing a storewide sale all weekend!!! 🛒🖤🛍 Now through Monday, December 2nd, get 20% off all of our ears and hair clips!!! 🎁  Don’t forget that we also offer free shipping on everything!!! 💖 \n•\n•\n•\n•\n• #mouseears #mickeyears #minnieears #disneyears #illusionears #3DEars #3dprintedears #3Dprintedmouseears #happilyeverhatter #shopsmall #girlboss #etsyshop #smallbusiness #blackfriday #supportsmallbusiness #smallbusinesssaturday",
    "Knitting is not just for Grandmothers!\nIt's also for Queens of Darkness!\n\nMEGA SALE !!!\n25% Rabatt auf alle meine Wolle, Garne usw.\nShop-Link: https://belisamawool.etsy.com/\n\n#Mulesingfrei #Weben #Häkeln #Unikat #Schafwolle #Wolleplastikfrei #forsale #sale #etsy #shop #HandgefärbtesStrickgarn #Schurwolle #handmade #Mulesingfree #weaving #Crochet #giftforknitters #Sheepwool #Germanwool #forsale #discount #etsyshop #25percent #xmas #Gift #present #Christmas #blackfridaydeals #blackfriday #BlackFriday2024",
    "Ricky Pearsall Signed Speed Mini Helmet - $120.00\nFred Warner Signed Eclipse Mini Helmet - $120.00\nFred Warner Signed Flash Mini Helmet - $125.00\nBrandon Aiyuk Signed Speed Mini Helmet - $135.00\n\nSpecial Black Friday Pricing * Limited Inventory * \nOffer good through Cyber Monday (expires 12/2/24 11:59pm)\n\nTo purchase email trifectacollectibles@gmail.com \nFirst to pay, claims the item. Will email payment options once inquiry is received. \n\n#rickypearsall #fredwarner #brandonaiyuk #49ers #blackfriday #sale #49ers #sf49ers #ninerempire #niners #ninersfaithful #ninergang #49erempire #49ersnation #49ersfaithful #bangbangninergang",
    "#blackfriday  with the Zwarte Raaf van @hertogjan.nl  Proeftuin….. #untappdreview #blackbeer",
    "🖤BLACK WEEKEND 2🖤\nPor solo 3 días estarán vaaarios productos seleccionados a un precio increíble ✨\n\n2. Medias negras - Unitalla (S-L) \n3. Set pijama con pantalón - Talla S, M, L y XL \n4. Medias blancas con rojo - Unitalla (S-L) \n5. Pijama Silky - Talla S, M, L, XL, 2XL, 3XL\n6. 5 panties sin costura - Talla L/XL\n\n📦Envió a todo El Salvador\n📍 Servicio PICK UP puedes recoger tu pedido en San Marcos\n\n#statussv #blackfriday #lencería #pijamas #panties",
    "#blackfriday #sisterdate 💯💯",
    "Don't miss out on our amazing Black Friday and Small Business Saturday event at Ace Hardware! Enjoy a fabulous 25% discount on all items in our gift section - the perfect opportunity to get a head start on your holiday shopping. Hurry in-store or shop online at www.mycoastalace.com 🎁🛠️ #BlackFriday #SmallBusinessSaturday #SalemisAceHardware #RockportFulton (Please note: Excludes Consuela)",
    "You've heard of Black Friday, but here's the REAL deal behind Black Friday! Tune in!\n\nListen at the Substack | YouTube | #podcast links in bio!\n\n#bible #inspiration #motivation #motivational #inspirational #MentalHealth #mentalhealthawareness #MoMo634 #selflove #selfcare #depression #anxiety #prayer #endthestigma #BlackFriday",
    "Don't miss out on our amazing Black Friday and Small Business Saturday event at Ace Hardware! Enjoy a fabulous 25% discount on all items in our gift section - the perfect opportunity to get a head start on your holiday shopping. Hurry in-store or shop online at www.mycoastalace.com 🎁🛠️ #BlackFriday #SmallBusinessSaturday #SalemisAceHardware #RockportFulton (Please note: Excludes Consuela)",
    "Don't miss out on our amazing Black Friday and Small Business Saturday event at Ace Hardware! Enjoy a fabulous 25% discount on all items in our gift section - the perfect opportunity to get a head start on your holiday shopping. Hurry in-store or shop online at www.mycoastalace.com 🎁🛠️ #BlackFriday #SmallBusinessSaturday #SalemisAceHardware #RockportFulton (Please note: Excludes Consuela)",
    "Take a little break from your #blackfriday shopping and grab a quick bite to eat with us!",
    "¡Llévate productos exclusivos y ofertas increibles en nuestro sitio web! \n\nDescuento exclusivo de la Colección Freedom:\n15%OFF - 1 Artículo\n20%OFF - 2 Artículos\n25%OFF - 3 Artículos\n\nNuestros descuentos son T O D O lo que has estado esperando\n\n#Heritage #LeatherBags #Blackfriday #CyberMonday #Freedom",
    "The iconic #summit cone of Liberty today in the clouds with a windchill in the high teens. #newhampshire #NH48 #newengland #603 #wmnfhikers #whitemountains #hiking #hikingadventures \n.\n.\n.\n#blackfriday #optoutside #mountains #snow #outside #outdoors #explore #autumn #winter #adventure #naturephotography #nature #travel #vista #winterwonderland #hikethewhites #appalachiantrail",
    "Venha aproveitar nosso FRETE GRÁTIS para compras acima de R$ 120,00\n•\nPromoção válida até domingo dia 01/12\n•\n•\n#blackfriday #promoção #artesanato #Natal #presentear #listadepresentes",
    "If you love our cute kinis from ESSENTIAL SOLIDS 💗 this is the opportunity to get it for only $20 at BLACK FRIDAY 🥂⁣\n\n#blackfriday #blackfridaydeals #bikinisale #deals #hawaii",
    "Who y’all would do this for 😭 #mystink #wigshopping #explore #funny #reels #blackfriday",
    "Black Friday Weekend: Share the Gift of Wellness\n\nIndulge in relaxation and self-care this holiday season. Gift a massage or facial to your loved ones and inspire them to prioritize their well-being.🎁🌿\n\n🔗 https://www.handandstonepleasantgrove.com/\n\n#BlackFriday #GiftOfWellness #HandAndStone #SelfCare #HolidayGifts",
    "✨ TODAY ONLY: Treat someone special (or yourself) with 25% OFF digital gift cards. Available to use at 40+ restaurants from NYC to Philly, DC, Florida, and soon... Nashville! \n\nThe clock's ticking ⏳—shop now via the link in bio!\n\n#uplandnyc #starrrestaurants #BlackFriday\nblurb on company who does our florals?",
    "🚨 Black Friday SALE Alert! 🚨\n\nWe have something for everyone! Whether you’re looking for:\n✨ All-day energy\n✨ Weight loss & inches off\n✨ Mood support & mental clarity\n✨ Better sleep\n✨ Glowing beauty products\n✨ Or even goodies for your pets…\n\nThis is your chance to snag it all during our epic Black Friday sale! 🎉\n\n💥 BOGO ends TONIGHT 💥\nPLUS, start your very own biz for just $4—it’s a life-changing opportunity that anyone can do. 🙌\n\nDon’t wait—this is YOUR moment to feel amazing, look incredible, and maybe even start building your dream future. DM me NOW to grab these deals before they’re gone! 💌\n\n#BlackFriday #BOGO #LifeChanging #StartFor4",
    "This black friday sale is bullshit, there is nothing good on sale!!!"
  ]
    return {"data": data}


# Send the data for sentiment analysis
@app.post("/analyze_sentiment")
async def analyze_sentiment():
    
    data = await get_data()

    captions = get_captions(data["data"])

    # Define headers for the request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"{groq_api_key}",
    }

    # Prompt template for the API
    prompt = (
        "Perform a thorough sentiment analysis of the above caption \n"
        "Format the output as follows in json format and directly give the json format, do not give any text only the metrics:"
        "{\"sentiment\": (positive or negative or neutral),\"score\": (ranging from 0.0 to 1.0, for negative score should be 0.0 to 0.4, positive should be 0.6 to 1.0 and neutal 0.4 to 0.6),\"positive_word_count\": ,\"negative_word_count\": }"
        "Strictly follow the format; do not add additional information for any of the metrics."
    )

    # Process each caption
    results = []
    for caption in captions:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json={
                "model": "llama3-70b-8192",
                
                "messages": [{"role": "user", "content": f"{caption}\n{prompt}"}]
            }
        )

        # Extract JSON data from the response
        try:
            response_json = response.json()  # Parse JSON from the response
            content = response_json.get('choices', [{}])[0].get('message', {}).get('content', None)
            match = re.search(r'\{.*?\}', content, re.DOTALL)
            if match:
                content = match.group(0)  # Extract the matched JSON-like string
                json_object = json.loads(content)  # Convert the string to a JSON object
                results.append(json_object)
            else:
                print(f"Error: No JSON object found in response for caption: {caption}")
        except Exception as e:
            print(f"Error processing caption '{caption}': {e}")
            
    # print(results)
    
    # Return the aggregated results
    return {"results": results}

    # Sample results
    # {
    # "results": [
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 5,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.83,
    #     "positive_word_count": 7,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 7,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 7,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "neutral",
    #     "score": 0.55,
    #     "positive_word_count": 4,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "neutral",
    #     "score": 0.5,
    #     "positive_word_count": 2,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 7,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "neutral",
    #     "score": 0.5,
    #     "positive_word_count": 0,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 7,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.7,
    #     "positive_word_count": 7,
    #     "negative_word_count": 2
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 5,
    #     "negative_word_count": 1
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 7,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 3,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 7,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "neutral",
    #     "score": 0.55,
    #     "positive_word_count": 7,
    #     "negative_word_count": 1
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 6,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 6,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "neutral",
    #     "score": 0.55,
    #     "positive_word_count": 2,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 7,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 7,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "positive",
    #     "score": 0.8,
    #     "positive_word_count": 14,
    #     "negative_word_count": 0
    #     },
    #     {
    #     "sentiment": "negative",
    #     "score": 0.2,
    #     "positive_word_count": 0,
    #     "negative_word_count": 4
    #     }
    # ]
    # }
