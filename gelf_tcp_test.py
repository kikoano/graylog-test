import logging
import graypy

users = [{"first":"Kennedi","last":"Wyman","email":"Kennedi.Wyman@camryn.name","address":"660 Elda Alley","created":"June 8, 2013","balance":"$4,719.24"},{"first":"Marina","last":"Schoen","email":"Marina.Schoen@constance.net","address":"567 Schuppe Mill","created":"October 16, 2011","balance":"$1,394.48"},{"first":"Cassidy","last":"McCullough","email":"Cassidy.McCullough@kathleen.org","address":"70703 Ed Shoals","created":"July 19, 2012","balance":"$8,895.85"},{"first":"Gino","last":"Spencer","email":"oliverabbit26@gmail.com","address":"26017 Schultz Corner","created":"February 6, 2019","balance":"$9,768.99"},{"first":"Hailey","last":"Reichel","email":"Hailey.Reichel@abelardo.info","address":"70288 Jazlyn Stravenue","created":"April 18, 2016","balance":"$1,590.53"},{"first":"Davonte","last":"Ferry","email":"Davonte.Ferry@lukas.name","address":"605 Brown Oval","created":"March 30, 2015","balance":"$4,614.46"},{"first":"Shakira","last":"Spencer","email":"Shakira.Spencer@erwin.com","address":"888 Grimes Square","created":"June 22, 2013","balance":"$9,022.01"},{"first":"Gonzalo","last":"Reichel","email":"Gonzalo.Reichel@fleta.biz","address":"415 Celestino Roads","created":"February 18, 2014","balance":"$7,952.32"},{"first":"Branson","last":"Turner","email":"plumwolf32@gmail.com","address":"524 Leda Stream","created":"August 12, 2014","balance":"$6,640.82"},{"first":"Stanford","last":"Thompson","email":"Stanford.Thompson@hermann.net","address":"87214 Aaliyah Forest","created":"December 28, 2018","balance":"$2,487.85"},{"first":"Cordelia","last":"Abbott","email":"Cordelia.Abbott@kody.net","address":"556 Alejandra Field","created":"July 29, 2012","balance":"$9,917.28"},{"first":"Darion","last":"Hermann","email":"Darion.Hermann@tyree.org","address":"336 Stanley Ferry","created":"September 17, 2017","balance":"$4,948.99"},{"first":"Larry","last":"D'Amore","email":"Larry.D'Amore@reagan.net","address":"60727 Mayert Radial","created":"July 12, 2016","balance":"$5,522.04"},{"first":"Lilian","last":"Powlowski","email":"Lilian.Powlowski@esta.name","address":"57971 Blick Turnpike","created":"April 9, 2013","balance":"$2,317.82"},{"first":"Tevin","last":"Mosciski","email":"Tevin.Mosciski@alta.net","address":"167 Buck Knolls","created":"June 18, 2018","balance":"$5,299.95"},{"first":"Anibal","last":"Stehr","email":"mintgreenwolf78@gmail.com","address":"893 Green Grove","created":"March 30, 2013","balance":"$9,736.33"},{"first":"Louvenia","last":"Howell","email":"oliveturtle83@gmail.com","address":"1533 Sage Neck","created":"December 12, 2011","balance":"$8,047.81"},{"first":"Bertram","last":"Sanford","email":"limesquirrel90@gmail.com","address":"233 Crooks Ville","created":"August 29, 2018","balance":"$9,023.23"},{"first":"Mya","last":"Bayer","email":"Mya.Bayer@marcel.net","address":"39013 Cristina Union","created":"May 11, 2016","balance":"$7,176.53"},{"first":"Amaya","last":"Bernhard","email":"Amaya.Bernhard@meagan.name","address":"4214 Kade Ridges","created":"October 18, 2013","balance":"$6,781.33"},{"first":"Amari","last":"Crist","email":"orangefrog29@gmail.com","address":"76738 Cornelius Prairie","created":"December 1, 2013","balance":"$219.76"},{"first":"Cecilia","last":"Glover","email":"Cecilia.Glover@lance.biz","address":"335 Elenora Mount","created":"October 1, 2015","balance":"$3,419.61"},{"first":"Kevin","last":"Luettgen","email":"Kevin.Luettgen@maia.name","address":"9728 Kilback Spring","created":"February 19, 2017","balance":"$3,005.94"},{"first":"Cristal","last":"Shanahan","email":"indigosquirrel78@gmail.com","address":"729 Kozey Mission","created":"May 1, 2014","balance":"$8,267.85"},{"first":"Salvatore","last":"Runolfsdottir","email":"yellowrabbit32@gmail.com","address":"814 Bogan Circles","created":"July 23, 2016","balance":"$516.12"},{"first":"Dell","last":"Abshire","email":"Dell.Abshire@heber.org","address":"488 Shanahan Valleys","created":"October 19, 2010","balance":"$7,835.35"},{"first":"Raina","last":"Zieme","email":"Raina.Zieme@emerald.org","address":"9708 Rosalind Crossing","created":"June 20, 2018","balance":"$6,997.18"},{"first":"Arnaldo","last":"Lockman","email":"maroonfrog94@gmail.com","address":"049 Candace Mission","created":"July 8, 2010","balance":"$431.03"},{"first":"Moshe","last":"Weber","email":"greygiraffe48@gmail.com","address":"048 Delores Drives","created":"May 16, 2011","balance":"$345.14"},{"first":"Roberta","last":"Prohaska","email":"silverturtle50@gmail.com","address":"901 Bogan Squares","created":"September 13, 2014","balance":"$9,870.95"},{"first":"Maia","last":"Fay","email":"indigogiraffe27@gmail.com","address":"431 Anabel Hills","created":"January 19, 2018","balance":"$6,566.26"},{"first":"Elroy","last":"Simonis","email":"yellowfrog56@gmail.com","address":"7795 Franco Wells","created":"August 27, 2015","balance":"$6,266.45"},{"first":"Kayli","last":"Bins","email":"Kayli.Bins@gaetano.name","address":"975 Shaylee Forge","created":"March 21, 2013","balance":"$5,712.40"},{"first":"Rey","last":"Ratke","email":"Rey.Ratke@alena.com","address":"435 Burdette Stream","created":"September 1, 2017","balance":"$2,048.65"},{"first":"Lydia","last":"Eichmann","email":"maroonfrog79@gmail.com","address":"91105 Johnson Island","created":"October 2, 2014","balance":"$8,655.51"},{"first":"Nestor","last":"Brakus","email":"Nestor.Brakus@aaron.net","address":"0191 Hyman Ways","created":"April 5, 2011","balance":"$2,506.10"},{"first":"Benton","last":"Hartmann","email":"Benton.Hartmann@dasia.com","address":"18714 Pamela Pine","created":"March 26, 2017","balance":"$2,889.21"},{"first":"Flavio","last":"Rice","email":"yellowwolf47@gmail.com","address":"43732 Roberts Underpass","created":"February 15, 2019","balance":"$7,934.33"},{"first":"David","last":"Hartmann","email":"tanrabbit01@gmail.com","address":"5704 Pacocha Rue","created":"September 18, 2014","balance":"$2,830.03"},{"first":"Quinton","last":"Hudson","email":"bluegiraffe92@gmail.com","address":"991 Myra Branch","created":"May 24, 2017","balance":"$5,501.06"},{"first":"Jenifer","last":"Sauer","email":"Jenifer.Sauer@orion.com","address":"0683 Tom Path","created":"May 1, 2011","balance":"$6,059.09"},{"first":"Ebony","last":"Sawayn","email":"orchidfrog27@gmail.com","address":"5274 Bernier Mountain","created":"November 17, 2016","balance":"$4,898.69"},{"first":"Michel","last":"Wintheiser","email":"Michel.Wintheiser@marjory.org","address":"61663 Harvey Flats","created":"June 27, 2015","balance":"$9,935.23"},{"first":"Kelley","last":"Ullrich","email":"fuchsiarabbit57@gmail.com","address":"8458 Shayne Points","created":"March 9, 2012","balance":"$9,165.73"},{"first":"Connie","last":"Padberg","email":"silversquirrel15@gmail.com","address":"44206 Cody Rest","created":"July 2, 2013","balance":"$4,887.28"},{"first":"Ciara","last":"Spinka","email":"silverwolf80@gmail.com","address":"81278 Bashirian Port","created":"July 4, 2014","balance":"$3,566.93"},{"first":"Cielo","last":"Kozey","email":"Cielo.Kozey@ellie.info","address":"638 Amelia Highway","created":"August 14, 2015","balance":"$6,331.34"},{"first":"Sunny","last":"Williamson","email":"indigorabbit70@gmail.com","address":"73319 Ryann Drives","created":"September 25, 2014","balance":"$5,688.43"},{"first":"Era","last":"Wiegand","email":"plumfrog51@gmail.com","address":"4350 Ezekiel Prairie","created":"March 27, 2017","balance":"$8,159.10"},{"first":"Mckayla","last":"Terry","email":"whitesquirrel60@gmail.com","address":"18047 Jacques Way","created":"August 23, 2016","balance":"$5,162.55"},{"first":"Kelley","last":"Schmidt","email":"Kelley.Schmidt@karson.org","address":"03129 Schultz Groves","created":"July 16, 2016","balance":"$2,374.25"},{"first":"Mariela","last":"Price","email":"Mariela.Price@guy.net","address":"6645 Collier Lane","created":"August 31, 2010","balance":"$8,311.07"},{"first":"Yazmin","last":"Christiansen","email":"violetrabbit76@gmail.com","address":"25659 Verna Plain","created":"March 28, 2012","balance":"$8,487.16"},{"first":"Clifton","last":"Hand","email":"Clifton.Hand@aida.com","address":"825 Jakubowski Lights","created":"June 29, 2017","balance":"$78.05"},{"first":"Elmore","last":"Ritchie","email":"Elmore.Ritchie@kirsten.name","address":"042 Aufderhar Route","created":"December 25, 2018","balance":"$2,791.24"},{"first":"Kailee","last":"Koelpin","email":"Kailee.Koelpin@leonie.name","address":"51967 Tatyana Mission","created":"January 3, 2018","balance":"$3,861.12"},{"first":"Francis","last":"Bins","email":"blacksquirrel35@gmail.com","address":"5042 Lottie Port","created":"April 19, 2013","balance":"$9,291.42"},{"first":"Brennon","last":"Flatley","email":"tealturtle67@gmail.com","address":"6495 Haven Turnpike","created":"November 8, 2011","balance":"$9,844.74"},{"first":"Willis","last":"Carter","email":"Willis.Carter@orpha.net","address":"3932 Fadel Key","created":"December 30, 2010","balance":"$2,132.64"},{"first":"Karl","last":"Corwin","email":"azurefrog59@gmail.com","address":"18477 Wilton Roads","created":"October 1, 2010","balance":"$4,758.90"},{"first":"Gladyce","last":"Bailey","email":"azureturtle46@gmail.com","address":"0227 Grant Bypass","created":"September 9, 2017","balance":"$295.23"},{"first":"Kira","last":"Koss","email":"Kira.Koss@shyanne.net","address":"5072 Zita Court","created":"November 10, 2014","balance":"$7,934.11"},{"first":"Dedrick","last":"Gibson","email":"salmonsquirrel47@gmail.com","address":"35733 Veda Crossing","created":"August 22, 2016","balance":"$737.69"},{"first":"Molly","last":"White","email":"Molly.White@alek.net","address":"160 Ernesto Knolls","created":"November 13, 2014","balance":"$7,946.51"},{"first":"Richmond","last":"Botsford","email":"Richmond.Botsford@laila.net","address":"500 Alexis Mountains","created":"September 19, 2009","balance":"$8,891.12"},{"first":"Romaine","last":"Jenkins","email":"Romaine.Jenkins@alek.org","address":"6971 Lolita Centers","created":"March 17, 2019","balance":"$9,604.93"},{"first":"Else","last":"Schaefer",\
        "email":"fuchsiaturtle05@gmail.com","address":"64347 Eliseo Shore","created":"March 3, 2015","balance":"$5,741.94"},{"first":"Alejandra","last":"Bogisich","email":"blackgiraffe55@gmail.com","address":"304 Fisher Orchard","created":"June 11, 2014","balance":"$8,459.96"},{"first":"Sedrick","last":"Murazik","email":"Sedrick.Murazik@kyra.org","address":"1619 Bauch Ways","created":"August 31, 2014","balance":"$791.99"},{"first":"Raymond","last":"Eichmann","email":"tanfrog77@gmail.com","address":"18231 Emelia Port","created":"March 23, 2015","balance":"$2,983.79"},{"first":"Keeley","last":"Lind","email":"Keeley.Lind@queenie.name","address":"97172 Terry Freeway","created":"October 29, 2015","balance":"$9,443.68"},{"first":"Myra","last":"McLaughlin","email":"Myra.McLaughlin@griffin.info","address":"19448 Flatley Brooks","created":"August 8, 2015","balance":"$8,815.91"},{"first":"Kaleigh","last":"Douglas","email":"ivoryrabbit72@gmail.com","address":"904 Vaughn Throughway","created":"November 17, 2011","balance":"$7,132.19"},{"first":"Enrique","last":"Bruen","email":"Enrique.Bruen@alta.com","address":"5188 Terrell Mountain","created":"November 29, 2010","balance":"$8,421.37"},{"first":"Laila","last":"Nolan","email":"plumwolf93@gmail.com","address":"045 Schulist Park","created":"March 28, 2013","balance":"$7,197.23"}]
def sendTCPLog(message):
    my_logger = logging.getLogger('test_logger')
    my_logger.setLevel(logging.DEBUG)

    handler = graypy.GELFTCPHandler('10.0.75.1', 12201)
    my_logger.addHandler(handler)
    my_logger.debug(message)
def invalidEmail(user):
    my_logger = logging.getLogger('test_logger')
    my_logger.setLevel(logging.DEBUG)

    handler = graypy.GELFTCPHandler('10.0.75.1', 12201)
    my_logger.addHandler(handler)

    my_adapter = logging.LoggerAdapter(logging.getLogger('test_logger'),
                                   {'first': user["first"],'last':user["last"]})
    my_adapter.debug('Invalid email '+user["email"])
def logInTest():
    for user in users:
        sendTCPLog("Log in "+user["first"] + " "+user["last"])
def logOutTest():
    for user in users:
        sendTCPLog("Log out "+user["first"] + " "+user["last"])

logInTest()
logOutTest()
invalidEmail(users[0])
invalidEmail(users[7])
invalidEmail(users[2])
invalidEmail(users[5])