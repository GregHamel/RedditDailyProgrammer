#[4/1/2014] Challenge #156 [Easy] Simple Decoder -- April Fools!
#http://www.reddit.com/r/dailyprogrammer/comments/21w3lb/412014_challenge_156_easy_simple_decoder/

import re

inp = "Etvmp$Jsspw%%%%\
[e}$xs$ks%$]sy$lezi$wspzih$xli$lmhhir$qiwweki2$Rs{$mx$mw$}syv$xyvr$xs$nsmr\
mr$sr$xlmw$tvero2$Hs$rsx$tswx$er}xlmrk$xlex${mpp$kmzi$e{e}$xlmw$qiwweki2$Pix\
tistpi$higshi$$He$xli$qiwweki$sr$xlimv$s{r$erh$$ll$vieh$xlmw$qiwweki2$]sy$$o $ger$tpe}$epsrk\
f}$RSX$tswxmrk$ls{$}sy$higshih$xlmw$qiwweki2$Mrwxieh$tswx$}syv$wspyxmsr$xs$fi$}syv\
jezsvmxi$Lipps${svph$tvskveq$mr$sri$perkyeki$sj$}syv$glsmgi2$\
Qeoi$wyvi$}syv$tvskveq$$Wor$e}w$&Lipps$[svph%%%&${mxl$7$%$ex$xli$irh2$Xlmw${e}\
tistpi$fvs{wmrk$xli$gleppirki${mpp$xlmro$$ld${i$lezi$epp$pswx$syv$qmrhw2$Xlswi${ls$tswx$lipps\
{svph$wspyxmsrw${mxlsyx$xli$xlvii$%%%${mpp$lezi$rsx$higshih$xli$qiwweki$erh$ws$}sy$ger$\
tspmxip}$tsmrx$syx$xlimv$$!!!$wspyxmsr$mw$mr$ivvsv$,xli}$evi$nywx$jspps{mrk$epsrk${mxlsyx$ors{mrk-\
Irns}$xlmw$jyr2$Xli$xvyxl${mpp$fi$liph$f}$xlswi${ls$ger$higshi$xli$qiwweki2$>-"


def decoder(s):
    #s = "".join([chr(ord(letter)-(4%2)**2) for letter in s] )
    answer = "".join(re.findall('\$\$[^\$]+\$', s))
    print ( re.sub('\$+',"",answer) )

decoder(inp)



#print( "".join([chr(ord(letter)-4) for letter in inp] ) )

message = "April Fools!!!!Way to go! You have solved the hidden message. Now it is\
 your turn to joinin on this prank. Do not post anything that will give away this message.\
  Letpeople decode  Da the message on their own and  hh read this message. You  k\
   can play alongby NOT posting how you decoded this message. Instead post your solution\
    to be yourfavorite Hello world program in one language of your choice. Make sure your\
     program  Skn ays 'Hello World!!!' with 3 ! at the end. This waypeople browsing the challenge\
      will think  h` we have all lost our minds. Those who post helloworld solutions without the\
       three !!! will have not decoded the message and so you can politely point out their\
          solution is in error (they are just following along without knowing)Enjoy this fun.\
              The truth will be held by those who can decode the message. :)"