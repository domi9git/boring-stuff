def main():
    import json
    from time import sleep
    try:
        import requests
    except ImportError:
        print('you havent installed the requests module, exiting in 5 seconds')
        sleep(5)
        exit()
    import configparser
    import os
    config_file = configparser.ConfigParser()

    config_file["Settings"]={
            "catamount": 1,
            }
    if not os.path.exists("config.ini"):
        print("config file not found, generating...")
        with open("config.ini","w") as file_object:
            config_file.write(file_object)
        print("config file generated")
    config_file.read('config.ini')
    catamount = round(float(config_file['Settings']['catamount']))
    print('generating...\nnote that you can generate up to 10000 cat per month')
    if catamount > 20:
        print("catamount has exceeded maximum amount (20)")
        catamount = 20
    for n in range(catamount):
        cat = requests.get("https://api.thecatapi.com/v1/images/search")
        json = cat.json()
        url = json[0]['url']
        caturl = requests.get(url)
        counter = 0
        exists = True
        while exists == True:
            if os.path.exists("cat"+str(counter)+"."+url[-3]+url[-2]+url[-1]):
                counter += 1
            else:
                with open("cat"+str(counter)+"."+url[-3]+url[-2]+url[-1], "wb") as image_file:
                    image_file.write(caturl.content)
                exists = False

if __name__ == '__main__':
    main()