from db_model.mongodb import conn_mongodb
from datetime import datetime

class BlogSession():
    blog_page ={'A':'blog_A.html', 'B':'blog_B.html'}
    session_count = 0
    
    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time= now.strftime("%Y-%m-%d %H:%M:%S") #https://strftime.org
        
        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'session_ip': session_ip,
            'user_eamil': user_email,
            'page': webpage_name,
            'access_time' : now_time
            
        })