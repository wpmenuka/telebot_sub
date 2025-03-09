import os
import time
from datetime import datetime
import telebot
import threading
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

mv_user_list = {}
ms_user_id = {}

admin = [7197786824]


bot = telebot.TeleBot(os.getenv('TELEGRAM_API_KEY'))

# ඔබේ channel ID එක මෙතැන දමන්න (උදා: "@your_channel_username")
YOUR_CHANNEL_ID = "@LkSubOfficial"  # ඔබේ channel username එක මෙතැන යොදන්න

# ඔබේ group ID එක මෙතැන දමන්න (උදා: "-1001234567890")
YOUR_GROUP_ID = -1002442784134  # ඔබේ group ID එක මෙතැන යොදන්න (- සලකුණ සහිතව)

# User channel එකේ subscribe කර ඇති දැයි පරීක්ෂා කරන function එක
def is_subscribed(user_id):
    try:
        # Get chat member info for channel
        member = bot.get_chat_member(chat_id=YOUR_CHANNEL_ID, user_id=user_id)
        
        # Check if the user is a member of the channel
        # Possible statuses: 'creator', 'administrator', 'member', 'restricted', 'left', 'kicked'
        return member.status in ['creator', 'administrator', 'member', 'restricted']
    except Exception as e:
        print(f"Error checking channel subscription: {e}")
        return False

# User group එකේ සාමාජිකයෙක් දැයි පරීක්ෂා කරන function එක
def is_group_member(user_id):
    try:
        # Get chat member info for group
        member = bot.get_chat_member(chat_id=YOUR_GROUP_ID, user_id=user_id)
        
        # Check if the user is a member of the group
        return member.status in ['creator', 'administrator', 'member', 'restricted']
    except Exception as e:
        print(f"Error checking group membership: {e}")
        return False

# User channel එකේ හෝ group එකේ දැයි පරීක්ෂා කරන function එක
def has_access(user_id):
    return is_subscribed(user_id) and is_group_member(user_id)

def only_group(ms_type,userid):

    if ms_type == "supergroup":
        return True
        
    elif ms_type == "private" and userid in admin:
        return True
    else:
        return False
    
    
        


def search(name,user_id,msid):
    def baiscope():
        moviename2 = []
        moviehref2 = []
        
        #link generater
        linkgen = "https://www.baiscope.lk/?s="+name
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.baiscope.lk/",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
        try:
            res = requests.get(linkgen)
            #print(res)
            beso = BeautifulSoup(res.content , "lxml")
            #movie list

            fi = beso.find_all("h5",{"class":"elementor-post__title"})
            
            x = 0
            for i in fi:
                if x<10:
                    finda = i.find("a")
                    #print(finda)
                    findname = finda.text.strip()
                    findname = findname+"B"
                    findurl = finda.get("href")
                    mvname = findname.replace("Sinhala Subtitles","").strip()
                    moviename2.append(mvname)
                    moviehref2.append(findurl)
                x = x + 1
            #mv_user_list[user_id]=[{"movie_name":moviename2,"link":moviehref2}]
            #print(mv_user_list)
            return moviename2, moviehref2
            
        except Exception as e:
            print("error = ",str(e))
            return [], []

    def pirate():
        moviename2 = []
        moviehref2 = []
        
        #link generater
        linkgen = "https://piratelk.com/?s="+name
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.baiscope.lk/",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

        try:
            res = requests.get(linkgen)
            #print(res)
            beso = BeautifulSoup(res.content , "lxml")
            #movie list

            fi = beso.find_all("h2",{"class":"post-box-title"})
            
            x = 0
            for i in fi:
                if x<10:
                    finda = i.find("a")
                    #print(finda)
                    findname = finda.string
                    findname = findname+"P"
                    findurl = finda.get("href")
                    mvname = findname.replace("Sinhala Subtitles","").strip()
                    moviename2.append(mvname)
                    moviehref2.append(findurl)
                x = x+1
            #mv_user_list[user_id]=[{"movie_name":moviename2,"link":moviehref2}]
            #print(mv_user_list)
            return moviename2, moviehref2
            
            
        except Exception as e:
            print("error = ",str(e))
            return [], []

    def cineru():
        moviename2 = []
        moviehref2 = []
        
        #link generater
        linkgen = "https://cineru.lk/?s="+name
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.baiscope.lk/",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

        try:
            res = requests.get(linkgen)
            #print(res)
            beso = BeautifulSoup(res.content , "lxml")
            #movie list

            fi = beso.find_all("h2",{"class":"post-box-title"})
            
            x = 0
            for i in fi:
                if x<10:
                    finda = i.find("a")
                    #print(finda)
                    findname = finda.string
                    findname = findname+"C"
                    findurl = finda.get("href")
                    mvname = findname.replace("Sinhala Subtitles","").strip()
                    moviename2.append(mvname)
                    moviehref2.append(findurl)
                x = x+1
            
            #print(mv_user_list)
            return moviename2, moviehref2
        
        except Exception as e:
            print("error = ",str(e))
            return [], []


    bais_name,bais_link = baiscope()
    pira_name,pira_link=pirate()
    cine_name,cine_link=cineru()

    plus_name = bais_name+pira_name+cine_name
    plus_link = bais_link+pira_link+cine_link

    mv_user_list[user_id] = [{"movie_name":plus_name,"link":plus_link,"msid":msid}]
    

    #message id add
    

@bot.message_handler(func=lambda message:message.text.startswith("/find"))
def handle_find(message):
        try:
            #user id eka
            user_id = message.from_user.id
            

            #message eka text ekak widihata gannawa
            msid = message.message_id
            mess = message.text

            #chat type eka bot,group,channel
            type1 = message.chat.type
            if not only_group(type1,user_id):
                return

            


            #channel eke da kiyala check karanawa
            if not has_access(user_id):
                keyboard = telebot.types.InlineKeyboardMarkup()
                join_button = telebot.types.InlineKeyboardButton(
                    text="Join Now",
                    url="https://t.me/LkSubOfficial"  # Replace with your actual channel link
                )
                keyboard.add(join_button)
    
                bot.send_message(
                    chat_id=message.chat.id,
                    text="ම්ම්..🙄 ඔයා අපේ Main චැනල් එකට ජොයින් වෙලා නෑ..\n😥නැත්තන් subtitles ගන්න වෙන්නේ නෑ..🥲\n😊පහලින් තියන 'Join Now' බට්න් එක ඔබලා ගිහින් අපේ Main චැනල් එකට ජොයින් වෙලා එන්නකෝ..",
                    reply_markup=keyboard,
                    reply_to_message_id=message.message_id
                )
                
                return


            messsp = mess.replace("/find", "", 1)
            if messsp:
                message_movie = messsp.replace(" ","+")
                message_movie = message_movie[1:]
                #print(message_movie)


                #message id
                msid = message.message_id

                #user id
                

                searching_msg = bot.send_message(
                    chat_id=message.chat.id,
                    text="🔍 *චිත්‍රපටයේ උපසිරැස සොයමින් පවතී...*\n\n⏳ කරුණාකර මොහොතක් රැඳී සිටින්න\n🎬 ඔබේ සිංහල උපසිරැස සොයමින් පවතී⏳",
                    reply_to_message_id=msid
                )


                #print(msid)
                search(message_movie,user_id,msid)

                #check user in film list
                if user_id in mv_user_list:
                    mvlist1 = mv_user_list[user_id]
                    mvlist2 = mvlist1[0]
                    mv_name = mvlist2["movie_name"]

                    #movie thinawada balanawa list eke
                    if mv_name:
                        

                        #mv_list_make = ""
                        #for i,film in enumerate(mv_name,start=1):
                            #mv_list_make+= f"{i}.{film}\n"

                        #searching message delete
                        try:
                            bot.delete_message(chat_id=message.chat.id,message_id=searching_msg.message_id)
                        except:
                            pass

                        #movie button list make

                        keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
                        buttons=[]

                        for i,film in enumerate(mv_name,start=1):
                            button = telebot.types.InlineKeyboardButton(
                                text=film,
                                callback_data=f"movie_{i}_{user_id}"
                            )
                            buttons.append(button)
                        keyboard.add(*buttons)

                       
                        with open('lksub.jpg', 'rb') as photo:
                            sent_message = bot.send_photo(
                                chat_id=message.chat.id,
                                photo=photo,
                                caption="🎬 *LK SUB* 🇱🇰\n\n📽️ පහත ලැයිස්තුවෙන් ඔබේ චිත්‍රපටයේ උපසිරැස තෝරන්න\n👇 ඔබට අවශ්‍ය චිත්‍රපටයේ උපසිරැස මත Click කරන්න\n\n💯 සිංහල උපසිරැස ලබා ගත හැකිය",
                                reply_markup=keyboard,
                                reply_to_message_id=msid
                        

                        )
                        #bot yawana ms eke id eka
                        sent_message_id = sent_message.message_id

                        #add id ekata
                        
                        ms_user_id[user_id] ={"ms_id":sent_message_id}

                        
                        

                        # Add ms_id to mv_user_list without overwriting existing data
                        if user_id in mv_user_list:
                            mv_user_list[user_id][0]["ms_id"] = sent_message_id
                        else:
                            mv_user_list[user_id] = [{"movie_name": [], "link": [],"msid": [], "ms_id": sent_message_id}]

                        #print(mv_user_list)
                        


                    else:
                        try:
                            bot.delete_message(chat_id=message.chat.id,message_id=searching_msg.message_id)
                        except:
                            pass
                        bot.send_message(
                        chat_id=message.chat.id,
                        text=f"❗{messsp} චිත්‍රපටයේ උපසිරැස සොයාගැනීමට අසමත් විය!\n\n🎬 ඔබ සෙවූ චිත්‍රපටයේ උපසිරැස අපගේ දත්ත සමුදායේ නොමැත\n\n🔍 කරුණාකර වෙනත් චිත්‍රපටයක් සොයන්න හෝ චිත්‍රපටයේ නම පරීක්ෂා කර නැවත උත්සාහ කරන්න💡",
                        reply_to_message_id=msid
                    )
            else:

                bot.send_message(
                    chat_id=message.chat.id,
                    text="⚠️ දෝෂයක් සිදුවී ඇත!\n\n🎬 කරුණාකර ඔබට අවශ්‍ය චිත්‍රපටයේ නම සමඟ /find විධානය භාවිතා කරන්න\n\nඋදාහරණ: /find Avengers\n\n🔍 නිවැරදිව චිත්‍රපට නම ඇතුළත් කර නැවත උත්සාහ කරන්න",
                    reply_to_message_id=msid
                )
                
                
        except Exception as e:
            print(f"error{e}")

#button handler

@bot.callback_query_handler(func=lambda call: call.data.startswith("movie_"))
def handle_movie_selection(call):
    try:
        _, idx_str, user_id_str = call.data.split("_")
        user_id1 = int(user_id_str)
        idx = int(idx_str) - 1  # Convert to zero-based index
        #user id eka
        clicked_user_id = call.from_user.id
        #message id eka
        clicked_message_id = call.message.message_id
        #print(clicked_user_id)

        #message id eka harida balanawa
        ms1 = mv_user_list[clicked_user_id]
        ms2 = ms1[0]
        ms3 = ms2["ms_id"]
        ms_name_get = ms2["movie_name"]
        user_find_id = ms2["msid"]
        

        if int(clicked_user_id) in mv_user_list:
            if ms3==clicked_message_id:
                #print("samanai")
                link_bot = ms2["link"]
                link_number_name = link_bot[idx]
                ms_namepro = ms_name_get[idx]
                ms_name_last_number = ms_namepro[-1]
                #print(ms_name_last_number)
                #print(link_number_name)
                mv_name_zip = download_sub(link_number_name,ms_name_last_number,ms_namepro)

                        
                #upload zip
                        
                if os.path.exists(mv_name_zip):
                    with open(mv_name_zip, "rb") as zip_file:
                        bot.send_document(
                        chat_id=call.message.chat.id,
                        document=zip_file,
                        caption="🎬 **LK SUB** 🇱🇰\n\n✅ උපසිරැසි සාර්ථකව බාගත කරන ලදී!\n📁 සිංහල උපසිරැසි සමඟ ඔබේ චිත්‍රපටය රසවිඳින්න\n\n💻 @LkSubOfficial",
                        reply_to_message_id=user_find_id
                                        
                    )
                                    # Delete the ZIP file after sending
                    os.remove(mv_name_zip)
                else:
                    bot.send_message(
                    chat_id=call.message.chat.id,
                    text="🔥Failed to upload the ZIP file.",
                    reply_to_message_id=user_find_id
                )
            else:
                print("")
        else:
            print("")

            


                
       
    except Exception as e:
        print(f"eeeerror{e}")








#download sub and upload
def download_sub(link,what_site,movie_name):
    try:
        movie_name = movie_name.split("|")[0] + ".zip"
        if link:
            try:
                if what_site == "B":
                    res2 = requests.get(link)
                    sop = BeautifulSoup(res2.content,"lxml")
                    fisub = sop.find("a",{"class":"dlm-buttons-button dlm-buttons-button-baiscopebutton"})
                    gethr = fisub.get("href")

                    #movie name 
                    #movie_name = movie_name + ".zip"

                    res3 = requests.get(gethr)
                    with open(movie_name,"wb")as f:
                        f.write(res3.content)

                    return movie_name

                elif what_site == "P":
                    res2 = requests.get(link)
                    sop = BeautifulSoup(res2.content,"lxml")
                    fisub = sop.find("a",{"class":"download-link download-button aligncenter"})
                    gethr = fisub.get("href")

                    res3 = requests.get(gethr)
                    with open(movie_name,"wb")as f:
                        f.write(res3.content)
                    
                    return movie_name

                elif what_site == "C":
                    res2 = requests.get(link)
                    sop = BeautifulSoup(res2.content,"lxml")
                    fisub = sop.find("a",{"class":"download"})
                    gethr = fisub.get("data-link")

                    res3 = requests.get(gethr)
                    with open(movie_name,"wb")as f:
                        f.write(res3.content)
                    
                    return movie_name
                    
                
            except Exception as a:
                print()
            
            
    except Exception as e:

        print ()

#list clear
def clear_dictionaries_hourly():
    while True:
        # Sleep for 1 hour (3600 seconds)
        time.sleep(3600)
        
        # Clear the dictionaries
        mv_user_list.clear()
        ms_user_id.clear()
        
        # Log the clearing action
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Cleared mv_user_list and ms_user_id dictionaries")

# Start the cleaning thread when the bot starts
cleaning_thread = threading.Thread(target=clear_dictionaries_hourly, daemon=True)
cleaning_thread.start()

#...........................................................................................

#bot message handler
@bot.message_handler(commands=["start"])
def send_message(message):
    #group channel button 
    keyboard = telebot.types.InlineKeyboardMarkup()
    group = telebot.types.InlineKeyboardButton(
        text="🔰Join Group🔰",
        url="https://t.me/Lk_Sub"  # Replace with your actual channel link
    )
    channel = telebot.types.InlineKeyboardButton(
        text="💠Join Channel💠",
        url="https://t.me/LkSubOfficial"  # Replace with your actual channel link
    )
    keyboard.add(channel,group)


    with open("lksub.jpg","rb")as photo:
        bot.send_photo(
            chat_id = message.chat.id,
            photo=photo,
            caption="🎬 LK SUB 🇱🇰\n\n✅ ශ්‍රී ලංකාවේ හොඳම සිංහල උපසිරැසි බොට් ✅\n\n⭐ සිංහල උපසිරැසි සොයාගැනීමට මෙම බොට් එක භාවිතා කිරීමට ඔබට හැකිය.\n\n📌 *භාවිතය:*\n🔰find [චිත්‍රපටයේ නම] ලෙස භාවිතා කරන්න\n🔰උදාහරණ: `/find Avengers`\n\n🔍 උපසිරැසි සොයමින් සිටින විට, කරුණාකර ඉවසීමෙන් සිටින්න.\n\n🎯 චිත්‍රපටයට අදාළ සිංහල උපසිරැසි ලැයිස්තුවෙන් ඔබට අවශ්‍ය උපසිරැසි තෝරාගන්න.\n\n❤️ *LK SUB භාවිතා කිරීම ගැන ස්තූතියි!",
            reply_markup=keyboard,
            reply_to_message_id=message.message_id

        )


#dic clear
@bot.message_handler(commands=["clear"])
def send_message(message):
    try:
        user_id = message.from_user.id
        if user_id in admin:
            mv_user_list.clear()
            bot.send_message(
                chat_id = message.chat.id,
                text="☢Clear List⚠",
                reply_to_message_id=message.message_id
                
            )
    except Exception as e:
        print(f"error{e}")


        




bot.infinity_polling()




#{7197786824: {'ms_id': 192}}
