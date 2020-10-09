    #!/usr/bin/env python
    # coding: utf-8

    # In[25]:

def scrape():
    from bs4 import BeautifulSoup as bs
    import requests


    # In[26]:


    from splinter import Browser
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)


    # In[27]:


    url = "https://mars.nasa.gov/news/"
    browser.visit(url)


    # In[32]:


    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    type(soup)
    soup.find_all("li",class_="slide")
    html = browser.html
    soup2 = bs(html, 'html.parser')
    #print(soup2.prettify())


    # In[79]:


    soup2.find_all("li",class_="slide")
    soup3 = soup2.find_all("div", class_="image_and_description_container")[0]
    soup3.a.text.split(".")
    p_text = soup3.a.text.split(".")[0]
    t_text = soup3.a.text.split(".")[1]


    # In[115]:


    nasa = "https://www.jpl.nasa.gov"
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)


    # In[116]:


    html = browser.html
    soup = bs(html, 'html.parser')
    #print(soup.prettify())


    # In[118]:


    soup.find_all("article")
    img = soup.article["style"].split("'")[1]
    featured_image_url = nasa + img
    #from IPython.display import Image
    #Image(featured_image_url)


    # In[112]:


    facts = "https://space-facts.com/mars/"
    browser.visit(facts)


    # In[131]:


    import pandas as pd
    df = pd.read_html(facts)
    for i in range(3):
        df[i].to_html(classes="table table-striped")


    # In[168]:


    url3="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    usgs = "https://astrogeology.usgs.gov"
    browser.visit(url3)


    # In[179]:


    html = browser.html
    soup = bs(html, 'html.parser')
    #print(soup.prettify())


    # In[181]:


    img_url=[]
    for i in range(4):  
        sweet = soup.find_all("a", class_="itemLink product-item")[(2*i+1)]['href']
        browser.visit(usgs+sweet)
        html = browser.html
        soup2 = bs(html, 'html.parser')
        img_url.append(soup2.find_all("img", class_="wide-image")[0]["src"])


    # In[184]:


    scrapped_data = [
        {"Valles_Marineris_Hemisphere": usgs+img_url[3]},
        {"Cerberus_Hemisphere": usgs+img_url[0]},
        {"Schiaparelli_Hemisphere": usgs+img_url[1]},
        {"Syrtis Major_Hemisphere": usgs+img_url[2]},
        {"Paragraph_Text":p_text},
        {"Title_Text":t_text},
        {"Featured_Image_URL": featured_image_url}
    ]
    return scrapped_data

    # In[ ]:




