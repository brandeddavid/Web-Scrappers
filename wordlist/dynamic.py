from selenium import webdriver

browser = webdriver.Firefox()

url = 'https://www.vocabulary.com/lists/558097'

browser.get(url)

words = browser.find_elements_by_class_name('word')
definitions = browser.find_elements_by_class_name('definition')

with open('words.txt', 'a') as file:

    for word in words:

        file.writelines(word.text + '\n')

browser.close()

# words = 'act, apt, ask, bat, bad, bag, cat, cap, cab, dad, dab, Dan, fan, fat, fad, gap, gab, gal, gas, ham, has, had, hat, jab, jam, lab, lad, lag, lap, man, mad, mat, map, nap, pan, Pam, pad, pal, ran, ram, rag, rat, Sam, sad, sag, sat, sap, tab, tan, tad, tag, tap, van, vat, yam, zap, Ben, bed, beg, bet, den, fed, gem, get, gel, hen, hem, jet, Ken, keg, led, leg, let, men, met, net, pen, peg, pet, red, set, ten, Ted, vet, yet, wed, wet, bin, bid, big, bit, dim, did, dig, dip, fin, fig, fit, gin, gig, him, his, hid, hit, hip, jib, Jim, jig, jip, kin, Kim, kid, kit, lid, lit, lip, nip, pin, pig, pit, rim, rid, rig, rip, sin, sit, sip, tin, tip, win, wit, zip, zit, bop, con, cod, cog, cot, cop, Don, dog, dot, fog, God, got, hog, hot, jog, jot, lob, log, lot, lop, mob, mom, mop, nod, not, pod, pot, rod, rot, son, sod, ton, Tom, tot, top, won, bun, bum, bus, bud, bug, but, cud, cut, cup, dug, fun, gun, gum, Gus, gut, hum, hug, hut, jug, jut, lug, mug, nun, nut, pun, pug, pup, rub, run, rum, rug, rut, sub, sun, sum, tug'
# words = words.split(',')
#
# with open('words.txt', 'a') as file:
#
#     for word in words:
#
#         file.writelines(word.strip() + '\n')
