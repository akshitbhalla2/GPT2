import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name = '124M')

gpt2.generate(sess, model_name = '124M')
