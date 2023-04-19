#7.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
#http://suninjuly.github.io/xpath_examples

css1= 'body > div:nth-child(3) > button:nth-child(3)'
css2='body div:nth-child(2)  .btn:nth-child(3)'
css3 ='body div:nth-child(2)  .btn:nth-last-child(2)'
css4 ='div:last-child button:nth-child(3)'
xpath1='/html/body/div[3]/button[3]'
xpath2='//button[text() = "Gold"]'
xpath3="//button[contains(text(), 'G')]"
xpath4='//div[2]/button[3]'
xpath5='//div[2]/button[last()-1]'
xpath6="//div[2]/descendant::button[3]"



#7.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
#http://suninjuly.github.io/cats.html

css5 = 'body > main > div > div > div > div:nth-child(5) > div > div > p'
xpath7 = '/html/body/main/div/div/div/div[5]/div/div/p'
css6='.col-sm-4:nth-child(5) p'

