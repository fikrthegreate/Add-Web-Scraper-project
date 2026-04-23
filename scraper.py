import requests
from bs4 import BeautifulSoup

def get_news():
    # መረጃ የምንወስድበት ድረ-ገጽ
    url = "https://www.bbc.com/news"
    
    try:
        # ድረ-ገጹን እንዲከፍትልን መጠየቅ
        response = requests.get(url)
        
        # የድረ-ገጹን ኮድ (HTML) መረዳት በሚችል መልኩ ማዘጋጀት
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # በ BBC ገጽ ላይ ያሉ የዜና አርዕስቶችን መፈለግ (h2 tag ውስጥ ስለሚገኙ)
        headlines = soup.find_all('h2')

        print(f"--- ከ {url} የተገኙ ዋና ዋና ዜናዎች ---\n")
        
        for index, i in enumerate(headlines[:10], start=1):
            print(f"{index}. {i.text.strip()}")
            
    except Exception as e:
        print(f"ስህተት አጋጥሟል: {e}")

# ፕሮግራሙን ማስጀመር
if __name__ == "__main__":
    get_news()