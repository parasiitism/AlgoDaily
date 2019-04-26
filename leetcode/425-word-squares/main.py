"""
    1st approach: trie + recursion

    Time    < O(nk + nk^2 + ...) < O(nk + n^n) k: average number of characters in words
    Space   O(n^n)
    660 ms, faster than 25.00%
"""


class TrieNode(object):
    def __init__(self):
        self.nodes = 26*[None]
        # to save time on startWith, we can cache the words when we traverse down the trie
        self.words = []


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        cur = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if cur.nodes[idx] == None:
                cur.nodes[idx] = TrieNode()
            cur = cur.nodes[idx]
            cur.words.append(s) # cache for startwith

    def startWith(self, s):
        cur = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if cur.nodes[idx] == None:
                return []
            cur = cur.nodes[idx]
        return cur.words


trie = Trie()
trie.insert("abc")
trie.insert("abd")
trie.insert("ace")
trie.insert("b")
trie.insert("bcd")
trie.insert("bce")
print(trie.startWith("a"))
print(trie.startWith("ab"))
print(trie.startWith("b"))
print(trie.startWith("bc"))

print("-----")

class Solution(object):

    def __init__(self):
        self.trie = Trie()
        self.res = []

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        for word in words:
            self.trie.insert(word)
        self.dfs(words, [], len(words[0]))
        return self.res

    def dfs(self, cands, chosen, k):
        if len(chosen) == k:
            if self.mightBeValidWordSquare(chosen):
                self.res.append(chosen)
            return

        newCands = []
        if len(chosen) == 0:
            newCands = cands[:]
        else:
            """
            e.g.
            ball
            area
            lead
            lady
            
            - on the 2nd col, we look for words start with a
            - on the 3nd col, we look for words start with le
            - on the 4th col, we look for words start with lad
            """
            i = 0
            n = len(chosen)
            prefix = ""
            while i < n:
                prefix += chosen[i][n]
                i += 1
            newCands = self.trie.startWith(prefix)

        for i in range(len(newCands)):
            # each string can be used once times
            # self.dfs(cands[:i]+cands[i+1:], chosen + [cands[i]], k)
            # -------------------------
            # each string can be used many times
            self.dfs(newCands, chosen + [newCands[i]], k)

    def mightBeValidWordSquare(self, words):
        n = len(words)
        for i in range(n):
            for j in range(n):
                if words[i][j] != words[j][i]:
                    return False  # not equal
        return True

a = ["area", "lead", "wall", "lady", "ball"]
print(Solution().wordSquares(a))

a = ["abat", "baba", "atan", "atal"]
print(Solution().wordSquares(a))

a = ["buff","ulus","buns","rump","cuts","stum","murk","wuss","putt","pubs","bust","chub","burp","bubs","suns","puns","buhr","ughs","mums","cunt","bhut","guff","pung","phut","flux","snub","ruts","vugg","turd","hung","tups","xyst","puny","curr","curf","typy","busk","byrl","cusp","pups","pulp","duns","dunk","tugs","dull","bury","murr","slum","mumm","jugs","burn","purl","curl","runt","spry","typp","fugu","dunt","mump","cuds","juju","sudd","nuts","culm","dumb","gyps","buzz","surf","putz","tung","tuns","puds","urns","tuck","duct","hugs","jump","bums","lulu","myth","rynd","undy","hunh","gulf","guts","lutz","burl","lump","dung","gull","gush","bunk","tusk","dups","stub","gust","curs","juts","swum","luff","subs","psst","syph","junk","funs","flub","hurt","burg","muck","buts","furl","such","mull","huff","chug","kuru","dubs","guls","drum","bunt","blub","rhus","buss","hump","rust","stud","fund","cubs","plum","punk","brut","cuff","sugh","wyns","pugh","cuss","buhl","hulk","burd","lurk","hymn","shun","yurt","puts","scum","luny","muns","lung","glug","hunk","guru","cyst","sump","slut","bull","gnus","thud","spur","cups","hunt","busy","yups","durr","turf","guck","full","sulk","purr","smut","curn","butt","suqs","duly","fuds","curb","chum","husk","upby","crud","grum","mugg","scut","thru","vugs","urbs","pump","bulb","smug","kudu","sync","punt","gyms","ruly","frug","crus","tuft","must","bund","ruff","rugs","push","mush","drys","rung","slub","bulk","dust","puck","shut","yuch","gunk","shul","tuts","purs","luck","whys","surd","rubs","dump","numb","thus","buck","duff","duds","gums","muds","sums","hull","thug","bung","musk","lynx","dusk","huts","puff","bump","wych","fugs","runs","jury","tump","bumf","huns","lunk","guys","sunk","lull","buds","glut","bush","knur","pull","sung","muff","funk","plug","ugly","snug","bugs","rush","lush","wynd","furs","curd","suds","hurl","muss","umps","slug","rums","urds","bunn","slur","blur","fuzz","stun","luvs","pugs","yuck","suss","scry","turk","mutt","muts","glum","sulu","mugs","grub","much","plus","buys","tuff","burs","cull","just","urus","drub","hums","null","fury","tsks","scup","lunt","sunn","tutu","lugs","curt","vugh","sups","nuns","trug","durn","nurd","puss","lums","mumu","nurl","cusk","drug","cult","gulp","club","puls","brrr","scud","huck","fuss","turn","fuck","tubs","ruth","ruby","duty","nubs","cwms","guvs","crux","suck","spud","rusk","dugs","wynn","hubs","futz","tush","rudd","pfft","hush","burr","hyps","ruck","fumy","yuks","duck","lust","guns","spun","fubs","flus"]
print(Solution().wordSquares(a))

a = ["ulus","mity","wind","chip","pill","pugh","flux","crib","sump","piss","fils","high","pipy","rusk","cuss","miri","pung","this","knit","hisn","zins","puns","tuff","ruth","whit","wild","burd","hubs","grin","kirs","zips","migg","lump","dint","jiff","spud","pith","rill","twit","pugs","ichs","jugs","simp","crus","bury","lisp","bund","fugs","prig","dusk","dirt","inns","mild","dups","hins","nigh","ring","muds","bisk","spin","tuts","puff","jill","grig","gist","bilk","gill","buck","slur","limn","firn","surf","girl","brit","ilks","typy","yirr","whir","undy","nill","rifs","husk","flus","sift","bids","swig","fuds","bush","birr","buff","buds","sims","ywis","suck","slit","irid","guck","fist","kris","dunk","didy","iffy","snub","luny","dull","stub","spic","buts","viny","bris","tump","phut","will","guff","putt","whid","tilt","slub","sris","pfft","mull","bill","turk","kith","grip","stun","hilt","skip","piny","curl","liri","lust","mirk","birl","musk","huts","tiff","tuns","ruin","burs","girn","juju","fuji","writ","suqs","much","iglu","lulu","bulb","gild","whig","yips","lips","riff","libs","gird","tils","whin","thru","tubs","hint","mumm","till","grid","bird","curb","rung","flit","glug","gimp","fink","sins","find","tick","mill","null","flip","cigs","subs","pits","tipi","zinc","skid","plus","grit","gnus","curf","turn","tiny","miff","gibs","nick","shit","linn","tint","bull","urbs","immy","gush","fury","tins","duff","wiss","pick","chum","junk","vugs","limb","sulk","kilt","buss","curr","ping","snug","tidy","khis","mids","with","frug","jinn","yill","fill","gulf","mush","list","swum","kink","cwms","quid","lunk","chug","urus","sulu","lutz","just","funk","firs","mixt","guts","gyps","yids","brin","silt","wigs","gigs","diss","mitt","hung","ribs","bhut","drum","pups","idly","pins","titi","ritz","slim","spik","furl","tics","sirs","must","shul","tips","burr","shin","suss","rush","lull","lift","zits","milk","puds","phiz","mick","tirl","nidi","film","ruts","stir","lung","pulp","lunt","ughs","sips","mibs","pily","kirn","glim","pirn","silk","luff","syph","birk","thin","butt","hums","smug","twin","kits","rink","tuft","wins","wuss","lush","tivy","unit","dump","duly","pity","hulk","trig","grub","curn","duns","kids","wist","tsks","flic","gits","mini","wing","zing","frig","lick","nixy","swim","yins","kiwi","nuns","cups","jism","vigs","puri","nurl","impi","quit","inly","syli","mugs","lurk","rims","spiv","duds","glum","dumb","rump","fixt","tyin","dips","bibs","wits","chub","king","buhr","virl","busy","scut","urns","scum","curs","gull","idyl","sync","smut","slum","sups","blin","suds","bubs","crud","firm","djin","sung","rich","runs","runt","suit","wink","bunn","pull","brut","slut","jibs","figs","gins","digs","wyns","hind","gips","mump","jigs","spur","dims","wynn","hips","nuts","dugs","ruck","sums","ding","nisi","girt","hunt","vill","clit","mutt","umps","gulp","puny","buys","trug","guid","duty","dits","spit","dung","yuch","guls","fumy","liny","prim","scud","shun","durr","ling","muns","rust","quiz","jibb","fuci","inti","guys","dirk","ills","whys","scry","ziti","crux","kind","huic","glut","sink","fubs","bind","ting","pigs","turd","tuis","gift","iwis","putz","kick","muss","mist","chid","kifs","ruly","mink","punk","skis","burn","lint","jump","pump","curt","bums","dink","murr","pimp","huns","fuzz","rimy","hull","yuks","fuck","fins","kuru","sudd","cuts","dipt","wynd","stum","city","nims","wily","sibs","unci","isms","psst","jink","bunt","pyic","ugly","sith","funs","myth","fibs","kudu","gilt","fuss","hunh","yurt","muts","rigs","rins","inks","rick","hiss","irks","puls","jinx","bulk","curd","purr","trip","such","hili","muck","hugs","vims","vugg","puss","limy","mils","midi","vugh","drub","hill","purl","huck","imid","duct","chit","miry","muni","litu","rift","kiln","buns","kips","tits","bitt","chis","fids","nurd","slip","rips","whiz","sics","brig","rhus","sing","dish","huff","rubs","sugh","sill","punt","lits","hurt","wiry","skim","hunk","cunt","plum","sunn","luvs","muff","brim","fizz","drib","piki","rynd","shiv","fisc","kirk","quin","sinh","pyin","purs","thud","knur","migs","grum","bins","burl","spun","blip","wych","cist","blub","icky","slid","wimp","lynx","tush","yuck","tusk","snit","hits","bits","grim","hump","mirs","mums","clip","fugu","skin","jury","cubs","pips","whip","pics","typp","lily","thir","mumu","smit","disc","pfui","blur","hymn","puts","wish","pink","bibb","gyms","bigs","tung","hick","puck","milt","itch","mind","cusk","uric","furs","guvs","guns","gink","nits","lich","shri","futz","duck","cris","duci","drip","illy","burp","minx","sild","brrr","lids","yird","guru","phis","wilt","fish","luck","link","psis","plug","bump","dins","lugs","burg","tuck","kill","jilt","wisp","drug","rugs","dust","shim","jimp","duit","push","pint","dill","disk","gyri","rind","lums","mint","ghis","rids","sizy","club","slug","scup","xyst","limp","imps","tups","sibb","cuff","tiki","stud","sits","nips","trim","bust","gums","wick","turf","fund","snip","cuds","fits","chin","tugs","inch","pish","hurl","thus","glib","murk","quip","flub","drys","dibs","pili","hyps","ruby","dick","bint","lins","wich","buhl","urds","zill","biff","kist","ibis","byrl","dubs","cull","puli","bumf","juts","gids","durn","surd","twig","friz","cusp","yups","hist","skit","kins","miss","nubs","chic","lilt","buzz","sign","frit","tutu","culm","sigh","whim","hush","bugs","winy","busk","inky","gunk","numb","sick","cult","risk","rudd","bunk","iris","ditz","inby","mugg","bung","zigs","rums","dirl","nils","pubs","jins","nibs","kiss","full","dunt","sunk","ship","pixy","suns","cyst","ruff","gust","thug","cuif","spry","snib","upby","shut"]
print(Solution().wordSquares(a))

a = ["ldqv","tibp","koey","dsdh","wxjz","glam","eyyy","ymeo","yjjp","qqjq","qsra","eldf","fcgc","fuqs","awgs","wcjp","pafp","amlz","uzql","rtre","sxur","frvx","lvwn","zbfv","ekfe","ugac","mqel","ryzg","uxfb","urea","vdir","xxeg","ipuq","vuxx","nzou","bsid","aows","schd","bkto","jrpm","cctl","koiu","vzaf","viuc","gnwm","sdvg","gvyu","bqkl","mtvj","wwpp","cyhe","hqpi","enoq","puhc","aknu","vwbg","bafk","bnhg","gcny","xdap","zmgr","pdpj","kpef","trms","miwe","bakx","vpbr","naiw","xlzj","bocb","tyyk","osqw","hhia","scer","igjz","tvsy","oron","tlqz","leyz","mgwb","ebbo","vmwm","nuxb","gunb","tjuj","oezm","spro","bjzo","jnjx","ucbu","yfpw","fmhl","xkfp","bnij","ihwn","fvci","isxg","svim","msyg","sjfs","rczg","vioc","ywrg","ebkr","noiu","hkhc","udtr","kxdf","qxgk","jziu","hjwb","oulh","kidq","mzks","rekt","pnye","bhup","vwwv","bxop","hyvv","aoae","ephf","fixl","jpjq","wzmb","ygzw","hyva","cjgu","ojxa","ovaw","jznc","duct","aotz","ryor","rchy","wktq","mwtt","ougt","lkks","zraz","jghv","oecr","icej","szfa","cilr","rhej","rgwm","mzws","lymr","htch","abva","vfhw","lgbz","igud","warz","grti","xycf","ffel","kqqs","pmyx","hxub","vdma","tdph","fxfw","drpf","yial","vgwr","uary","rdgu","kyoj","ygfg","yvet","muzi","vydu","sabk","cylc","eiys","ozfz","sdrq","xwnf","laqb","apfd","tqci","gpvm","qxbn","ednm","qara","iawb","lzvs","spvv","hdbq","mrgu","mkfy","hxdt","qczg","nxwy","uzlm","jfde","nwao","satz","ruoz","sruw","iwnk","dclt","smss","lhto","hihh","zrsq","xjfe","jxkf","wgpb","ptfl","hnjz","yxjq","yqyk","xeib","mjpo","blhi","xksx","smju","xazs","zujb","xrmt","nrgs","zimw","dove","rzjk","rhbl","doaz","pdnx","tktr","fgzd","jdcs","yuqv","tlch","mdak","fybt","ewzh","inza","qakq","zkma","rrga","falm","ngxs","xbda","xbdg","nsfm","uqvi","exft","eozp","fabz","azbc","wmpb","ctpn","udhn","yvxk","pqxr","zcde","zbsh","vgzv","qdot","ozeu","jcdn","uvri","maib","kxml","nytx","vwac","pzhx","poqa","vjeq","grph","skqt","eyak","yqle","yhpe","urmq","wmnj","eupp","juav","lzab","vpga","jmho","icpv","hgak","oqzp","jhce","trkw","foog","bnvj","teri","sevi","pgaf","hugy","llpn","xrcz","fjya","ydjh","ckzr","xhcn","eeyw","ckzx","ietb","gtah","wnut","knzc","ahvp","aqbh","dxmf","eeyc","wzwi","uakc","yeap","exyh","kanw","ygum","ytfn","hhak","wbrl","bvcb","ogzh","ufax","cvxp","jpkc","bhff","mgws","ybiz","daph","abhn","bvjf","xtma","ukuw","dapu","qigj","blmj","loic","mnaw","qlyv","ycsz","fkua","dhzg","ctwf","ejui","ayrt","wxiy","zsng","vjpq","gvjc","epyg","xnmk","rwaa","gjzb","jhqd","yurf","lwek","xnme","xyur","ufsd","bmhc","wwwc","atjg","voos","ofjq","owhc","oklh","dejn","lzdb","szla","mrxq","hssr","oicv","cads","oafg","uvvk","yonk","xohx","voic","wekh","yygg","odtz","criz","qcps","vxfg","thjz","gbgx","gkcq","bgjz","yxfy","yggl","lclm","rqbb","kftb","wekb","xzir","kmqv","fpwy","kipl","fvgt","kmqh","ovnm","rfiq","vhjo","hvcg","wpwf","rgvt","tkyl","zyyz","exkq","dynw","uvug","unqa","rjqm","nfsi","rogj","fqvr","zxtj","eamr","oxap","tmoh","qels","ntic","zmsu","htzi","lxbe","cemy","sxae","qppg","vndx","tbbc","jtjn","zezb","fctj","irud","vgkh","zsad","aeqn","pxsa","mywd","lktx","lyzn","uhqh","qheo","qylj","twxv","kffg","wrio","nebh","tsga","omfr","kkep","qgqe","bppz","ojrx","ilqs","fgcb","sayj","spga","qbtt","jnzf","uuxa","bsfw","djwd","jygn","tzwv","dmco","hofl","lrqy","thty","xibo","mgek","aexq","wgxs","eega","swcp","rvxo","essd","opxr","foph","yqqb","uqxh","tmtn","syac","rvxj","ycex","xwpi","lbih","jqwg","cfmy","erbk","ycku","fiej","oghu","erbo","uyug","nmif","denc","toik","owdd","hbxf","fhkh","jksd","dnbn","ujem","rlwc","oojq","vzqc","vsxh","wrzv","xmlu","qeiw","vebr","jgrz","bgdg","bjqc","xnuk","kwti","aiwc","evnv","gttd","ntma","ffdo","ublq","fjzw","cgya","jukv","hwvx","rblz","uyvg","gkil","ukoe","ainn","lekg","jwcc","xndl","tnvd","sskz","ibka","hkvn","jdno","yvir","kwvu","npzu","zwpe","mguj","gxsl","awfx","rlbe","dlxw","ehvp","gpuu","leud","dqet","tqkg","pwwe","lyqz","hcay","graj","jaqb","raxj","snfq","rpij","vffm","fnlo","ymki","etik","sipm","lkoi","tcnq","oxpd","kvac","yaxe","xmvv","izxo","foss","yzgd","dgub","gnhj","nqpg","htai","zbny","rlld","kmom","uyoy","joyw","mvcd","fcmm","gagc","qrdf","vprp","gkur","joyd","rvyz","ywip","tihz","udbx","hfhs","jxdo","vhtq","jmri","snpv","fvmi","yumq","mqhb","rccb","ixud","zhxb","bzoz","pkpb","opag","axzf","nlkk","ilmm","xqyu","xgvz","zxim","sjvz","wjsj","khew","oxjb","giri","tavh","xffa","aasl","zngx","ygoi","mvor","zdwq","yhwn","vxys","jbud","jxgu","kpkz","tmnk","xjxg","nqbg","zfwt","zpee","coqp","iyrz","zklv","dgvg","fbqo","vpkz","aijr","yeog","iyru","xemr","qqft","jtkj","omwr","vfbz","yizn","qqfs","dcip","whog","noeg","gwii","wkje","hhbz","exrl","cmyx","bulm","gjqy","uahk","davi","okjn","jhvc","gwwp","rvdu","eeqd","rsje","vlco","lhqj","bjdq","hnou","pqdf","jzbv","iobg","eyqb","hoam","rzzy","ctrc","hoab","yidi","ypup","mpqj","cjrf","kzib","xhvp","gimw","zsig","nlpm","mdxk","jftn","fkpj","eajd","pxbh","lyks","zopy","apcl","kxoo","ecpu","uzuc","jouj","kxog","cfdn","aktr","udfu","lgvc","oiny","uwci","fefg","oago","btdy","ofvg","vzla","fedn","cpts","ewfy","thkl","dfwm","xxgb","zqle","ungi","ngmr","ooip","fxdp","eviy","shjs","cuqu","ygan","qwvi","pwru","xnyc","wpvw","ojhz","okqg","nolf","kwht","osdv","kfwp","mmvr","skzx","mwda","dghb","bvvh","qlcu","adbc","hesk","rypw","dezb","jjqd","irbf","wqqi","tlwz","nwfx","ntuq","wqqu","zkvu","hdlw","hzfx","czvw","uqli","alum","zqgp","cbbk","lfeh","wagb","vrpl","snny","gfzg","chps","edyc","mzle","mpcg","qous","upyn","natl","ftco","ukmc","kbtf","upye","fgbf","frcm","ytdu","srlb","ycqu","pfbs","gamy","ditz","bceh","nedl","bmpc","xxab","uquk","gmvi","gamn","qtgn","imln","bvox","uela","xzza","ydsw","fqbu","zgoi","pfcu","pdil","kuln","aeyy","oade","wlco","euwh","dhsq","htii","blys","jtzg","yrvb","lcef","qrlq","dzcz","kbxs","urbt","xgqq","xasg","ucsu","hhqa","txzd","ozgk","mook","rohf","hojd","fema","gsfj","edby","lvdg","czxq","bbyl","yiwb","rkie","vedk","pueg","yksc","lvdm","ghsi","lswv","ttjt","rdaf","uezp","ndbp","lsbr","phel","anwe","mjcz","ngfs","mkei","tixh","oyvx","lxyx","xftd","aeol","iwaj","nnlg","trgg","gefc","bgln","nmnr","cmal","rqic","nnlp","rqif","slkq","ylzq","mazo","wepn","hqnd","hkmx","onxu","zukm","yrcp","qerl","dowl","ehsu","efyv","fzpi","mfny","vtfv","hzbw","zlvt","gjmv","smbe","wwhz","qzrz","ugml","rowz","pylj","nsji","imij","cjat","sojk","lzcy","jzcq","rowk","bcsz","ecqy","witq","kjxi","eeih","ymha","mzon","yjtl","vwws","kcwe","rvrf","pmph","uzvk","pxho","uszb","csox","byor","ovge","zotp","mebc","iisf","xjkm","zarv","nkfx","flih","jxbc","wisy","zptw","gtqn","orxa","wnum","ttlg","qsgz","cafz","eusu","cqqh","dmun","tnhw","royc","tftk","yagc","sftr","usfr","wcid","teza","isdg","ckog","dysy","rjbi","ltlm","mlol","yzsg","ptkt","doyr","rbri","okva","skiu","iwfr","ebfv","tojg","uvmr","pzbe","wnij","iezr","sdcg","kpan","mfec","cmfx","bfen","ulai","exrm","jaxf","vfdr","nxvk","iodt","vcdd","epbo","tbie","mnuw","qjay","edop","ioav","ohkj","ucmh","vqss","oavy","eeak","egwg","sljt","xnam","ffab","puse","znoq","pmhf","bjrl","syxs"]
print(Solution().wordSquares(a))