# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:56:53 2021

@author: user
"""

from ElGamal import *

q = 1367176787662174613885987459588219879372220953507
p = 123673323891242867177514096819580236465497274063458984325241055844011153224145054858864521371774649105018822971116982650715941117881035552815726337827743610567394319322651354827890393410346287094867949471330649611353144350280202803994699252851189649371736656279618955988650904092455232405972031238033017555179
g = 40462122118872181945378921352487072939516952018662735686055484614731377300241296793274194015330677874561913862257032349319195310454288579931897783172699368476617643935592066536592964203996764617393497763030102454645553889589858508155863659008244138450734103034330653704886415203645218198502091410748740351645
m1 = b'I am gonna make him an offer he cannot refuse'
r1 = 35813661127331527469358400061602362468584884055947523542303622721572499086663124962197759732570128299538504165559471799420230156151361355657687768842558207913000173070081545579782756759116180932498448390259402632002506904042755369723913250346319397461924695165447086327416600659876669982364749540300843612970
t1 = 43627224218115797228289249475921032907034220460492356111895503936082854418168250416497072941347471994743727973254642325585453584081740799906360299844041802654220328431411951616679346995559843264254628068501613292959454582118556805666347691733714922031589614165107379883775596944798653631705811795089241771123

r2 = 35813661127331527469358400061602362468584884055947523542303622721572499086663124962197759732570128299538504165559471799420230156151361355657687768842558207913000173070081545579782756759116180932498448390259402632002506904042755369723913250346319397461924695165447086327416600659876669982364749540300843612970
t2 = 5956813619278201140800924272068090554564909295979962450630656519740430477504942407392993409599925085203647233193851018647091657112428687538063606647173251762864208428373009582042639482695547913744731417387816335621025572344854442283807515125579921298217666328301529878649319957708915200631529408344007611288

if (r1 == r2):
    print("Same k is used for encryption which is a fatal!")   
m1_int = int.from_bytes(m1, byteorder='big') 
t1_inv = modinv(t1, p)
m2 = (t2*m1_int*t1_inv)%p
print("My message is following:", m2.to_bytes((m2.bit_length() + 7) // 8, byteorder='big').decode("UTF-8"))
                            