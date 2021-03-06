# pylint: disable=invalid-name,protected-access
from allennlp.common.testing import ModelTestCase

from my_library import *


class BiMPMTest(ModelTestCase):
    def setUp(self):
        super(BiMPMTest, self).setUp()
        self.set_up_model('tests/quora_bimpm_test.json',
                          'tests/quora_train_sample.tsv')

    def test_model_can_train_save_and_load(self):
        self.ensure_model_can_train_save_and_load(self.param_file)


class ParaClassificationTest(ModelTestCase):
    def setUp(self):
        super(ParaClassificationTest, self).setUp()
        self.set_up_model('tests/quora_para_classification_test.json',
                          'tests/quora_train_sample.tsv')

    def test_model_can_train_save_and_load(self):
        self.ensure_model_can_train_save_and_load(self.param_file)


class ParaCosineTest(ModelTestCase):
    def setUp(self):
        super(ParaCosineTest, self).setUp()
        self.set_up_model('tests/quora_para_cosine_test.json',
                          'tests/quora_train_sample.tsv')

    def test_model_can_train_save_and_load(self):
        self.ensure_model_can_train_save_and_load(self.param_file)


class ESIMTest(ModelTestCase):
    def setUp(self):
        super(ESIMTest, self).setUp()
        self.set_up_model('tests/quora_esim_word_char_test.json',
                          'tests/quora_train_sample.tsv')

    def test_model_can_train_save_and_load(self):
        self.ensure_model_can_train_save_and_load(self.param_file)


class ESIMCosineTest(ModelTestCase):
    def setUp(self):
        super(ESIMCosineTest, self).setUp()
        self.set_up_model('tests/quora_esim_cosine_word_char_test.json',
                          'tests/quora_train_sample.tsv')

    def test_model_can_train_save_and_load(self):
        self.ensure_model_can_train_save_and_load(self.param_file)
