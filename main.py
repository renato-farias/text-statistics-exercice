text_input = "lorem ipsum dolor sit amet consectetur lorem ipsum et mihi quoniam et adipiscing elit.sed quoniam et advesperascit et mihi ad villam revertendum est nunc quidem hactenus ex rebus enim timiditas non ex vocabulis nascitur.nummus in croesi divitiis obscuratur pars est tamen divitiarum.nam quibus rebus efficiuntur voluptates eae non sunt in potestate sapientis.hoc mihi cum tuo fratre convenit.qui ita affectus beatum esse numquam probabis duo reges constructio interrete.de hominibus dici non necesse est.eam si varietatem diceres intellegerem ut etiam non dicente te intellego parvi enim primo ortu sic iacent tamquam omnino sine animo sint.ea possunt paria non esse.quamquam tu hanc copiosiorem etiam soles dicere.de quibus cupio scire quid sentias.universa enim illorum ratione cum tota vestra confligendum puto.ut nemo dubitet eorum omnia officia quo spectare quid sequi quid fugere debeant nunc vero a primo quidem mirabiliter occulta natura est nec perspici nec cognosci potest.videmusne ut pueri ne verberibus quidem a contemplandis rebus perquirendisque deterreantur sunt enim prima elementa naturae quibus auctis virtutis quasi germen efficitur.nam ut sint illa vendibiliora haec uberiora certe sunt.cur deinde metrodori liberos commendas.mihi inquam qui te id ipsum rogavi nam adhuc meo fortasse vitio quid ego quaeram non perspicis.quibus ego vehementer assentior.cur iustitia laudatur mihi enim satis est ipsis non satis.quid est enim aliud esse versutum nobis heracleotes ille dionysius flagitiose descivisse videtur a stoicis propter oculorum dolorem.diodorus eius auditor adiungit ad honestatem vacuitatem doloris.nos quidem virtutes sic natae sumus ut tibi serviremus aliud negotii nihil habemus."

from text_statistics import TextStatistics

def show_response(question, response):
    print(question)
    print(f"R: {response}")
    print()

if __name__ == "__main__":
    ts = TextStatistics(text_input=text_input)
    show_response("How many words are there in the text?", ts.num_of_words)
    show_response("How many sentences are there in the text?", ts.num_of_sentences)
    show_response("What is the length of the longest word?", f"word: {ts.longest_word.word}, len: {ts.longest_word.len}")
    show_response("Which six words occur the most in the text?", ts.top_repeated_words(top_of=6))
    show_response("What percentage of the words, excluding duplicates, only occur once?", ts.only_once_percentage)
    show_response("What is the average number of words per sentence?", ts.average_of_words_per_sentence)
    show_response("Which three two-word phrases occur the most in the text?", ts.get_top_x_word_sentences(num_of_words=2, top_of=3))
