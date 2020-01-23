"""Test suite for textstat
"""

import textstat


def test_char_count(long_text):
    textstat.set_lang("en_US")
    count = textstat.char_count(long_text)
    count_spaces = textstat.char_count(
        long_text, ignore_spaces=False
    )

    assert count == 1750
    assert count_spaces == 2123


def test_letter_count(long_text):
    textstat.set_lang("en_US")
    count = textstat.letter_count(long_text)
    count_spaces = textstat.letter_count(
        long_text, ignore_spaces=False
    )

    assert count == 1688
    assert count_spaces == 2061


def test_lexicon_count(long_text):
    textstat.set_lang("en_US")
    count = textstat.lexicon_count(long_text)
    count_punc = textstat.lexicon_count(long_text, removepunct=False)

    assert count == 372
    assert count_punc == 376


def test_syllable_count(long_text):
    textstat.set_lang("en_US")
    count = textstat.syllable_count(long_text)

    assert count == 521


def test_sentence_count(long_text):
    textstat.set_lang("en_US")
    count = textstat.sentence_count(long_text)

    assert count == 16


def test_avg_sentence_length(long_text):
    textstat.set_lang("en_US")
    avg = textstat.avg_sentence_length(long_text)

    assert avg == 23.3


def test_avg_syllables_per_word(long_text):
    textstat.set_lang("en_US")
    avg = textstat.avg_syllables_per_word(long_text)

    assert avg == 1.4


def test_avg_letter_per_word(long_text):
    textstat.set_lang("en_US")
    avg = textstat.avg_letter_per_word(long_text)

    assert avg == 4.54


def test_avg_sentence_per_word(long_text):
    textstat.set_lang("en_US")
    avg = textstat.avg_sentence_per_word(long_text)

    assert avg == 0.04


def test_flesch_reading_ease(long_text):
    textstat.set_lang("en_US")
    score = textstat.flesch_reading_ease(long_text)

    assert score == 64.75

    textstat.set_lang("de_DE")
    score = textstat.flesch_reading_ease(long_text)

    assert score == 63.1

    textstat.set_lang("es_ES")
    score = textstat.flesch_reading_ease(long_text)

    assert score == 84.37

    textstat.set_lang("fr_FR")
    score = textstat.flesch_reading_ease(long_text)

    assert score == 80.31

    textstat.set_lang("it_IT")
    score = textstat.flesch_reading_ease(long_text)

    assert score == 89.27

    textstat.set_lang("nl_NL")
    score = textstat.flesch_reading_ease(long_text)

    assert score == 61.97

    textstat.set_lang("ru_RU")
    score = textstat.flesch_reading_ease(long_text)

    assert score == 116.45


def test_flesch_kincaid_grade(long_text):
    textstat.set_lang("en_US")
    score = textstat.flesch_kincaid_grade(long_text)

    assert score == 10.0


def test_polysyllabcount(long_text):
    textstat.set_lang("en_US")
    count = textstat.polysyllabcount(long_text)

    assert count == 32


def test_smog_index(long_text):
    textstat.set_lang("en_US")
    index = textstat.smog_index(long_text)

    assert index == 11.2


def test_coleman_liau_index(long_text):
    textstat.set_lang("en_US")
    index = textstat.coleman_liau_index(long_text)

    assert index == 9.35


def test_automated_readability_index(long_text):
    textstat.set_lang("en_US")
    index = textstat.automated_readability_index(long_text)

    assert index == 12.3


def test_linsear_write_formula(long_text):
    textstat.set_lang("en_US")
    result = textstat.linsear_write_formula(long_text)

    assert result == 14.5


def test_difficult_words(long_text):
    textstat.set_lang("en_US")
    result = textstat.difficult_words(long_text)

    assert result == 49


def test_difficult_words_list(short_text):
    textstat.set_lang("en_US")
    result = textstat.difficult_words_list(short_text)

    assert result == ["sunglasses"]


def test_dale_chall_readability_score(long_text):
    textstat.set_lang("en_US")
    score = textstat.dale_chall_readability_score(long_text)

    assert score == 6.87


def test_gunning_fog(long_text):
    textstat.set_lang("en_US")
    score = textstat.gunning_fog(long_text)

    assert score == 11.26

    # FOG-PL
    textstat.set_lang("pl_PL")
    score_pl = textstat.gunning_fog(long_text)

    assert score_pl == 10.40


def test_lix(long_text):
    textstat.set_lang("en_US")
    score = textstat.lix(long_text)

    assert score == 45.11


def test_rix(long_text):
    textstat.set_lang("en_US")
    score = textstat.rix(long_text)

    assert score == 5.13


def test_text_standard(long_text, short_text):
    textstat.set_lang("en_US")
    standard = textstat.text_standard(long_text)

    assert standard == "9th and 10th grade"

    standard = textstat.text_standard(short_text)

    assert standard == "2nd and 3rd grade"


def test_reading_time(long_text):
    textstat.set_lang("en_US")
    score = textstat.reading_time(long_text)

    assert score == 25.68


def test_lru_caching(short_text):
    textstat.set_lang("en_US")
    # Clear any cache
    textstat.sentence_count.cache_clear()
    textstat.avg_sentence_length.cache_clear()

    # Make a call that uses `sentence_count`
    textstat.avg_sentence_length(short_text)

    # Test that `sentence_count` was called
    assert textstat.sentence_count.cache_info().misses == 1

    # Call `avg_sentence_length` again, but clear it's cache first
    textstat.avg_sentence_length.cache_clear()
    textstat.avg_sentence_length(short_text)

    # Test that `sentence_count` wasn't called again
    assert textstat.sentence_count.cache_info().hits == 1


def test_changing_lang_clears_cache(short_text):
    textstat.set_lang("en_US")

    # Clear any cache and call reading ease
    textstat.flesch_reading_ease.cache_clear()
    textstat.flesch_reading_ease(short_text)

    # Check the cache has only been missed once
    assert textstat.flesch_reading_ease.cache_info().misses == 1

    # Change the language and recall reading ease
    textstat.set_lang("fr")
    textstat.flesch_reading_ease(short_text)

    # Check the cache hasn't been hit again
    assert textstat.flesch_reading_ease.cache_info().misses == 1


def test_unicode_support():
    textstat.set_lang("en_US")
    textstat.text_standard(
        "\u3042\u308a\u304c\u3068\u3046\u3054\u3056\u3044\u307e\u3059")

    textstat.text_standard("ありがとうございます。")


def test_spache_readability(easy_text):
    textstat.set_lang("en_US")
    spache = textstat.spache_readability(easy_text, False)

    assert spache == 2


def test_dale_chall_readability_score_v2(long_text):
    textstat.set_lang("en_US")
    score = textstat.dale_chall_readability_score_v2(long_text)

    assert score == 6.87


def test_default_lang_configs(long_text):
    # Config from default en_US should be used
    textstat.set_lang("en_GB")
    score = textstat.flesch_reading_ease(long_text)

    assert score == 64.75
