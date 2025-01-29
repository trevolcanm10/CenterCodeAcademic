from bs4 import BeautifulSoup
import requests
import pandas as pd
def main():
    #Accedemos a la url
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Guardamos titulos,links,scores
    titles = []
    links = []
    scores = []

    for item in soup.find_all('tr',class_='athing'):
        title_line = item.find('span', class_='titleline')
        if title_line:
            title = title_line.text
            title_link = title_line.find('a')
            link = title_link['href']
            #Etiquete similar
            score = item.find_next_sibling('tr').find('span',class_='score')
            if score:
                score = score.text
            else:
                score = "None"
            titles.append(title)
            links.append(link)
            scores.append(score)
        else:
            print("No se encontró un título para el elemento, se omite.")

    df = pd.DataFrame(
        {
            'Title': titles,
            'Link': links,
            'Score': scores
        }
    )

    print(df)
if __name__== "__main__":
    main()
