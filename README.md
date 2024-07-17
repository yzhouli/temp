# Experimental Settings

**Platform Settings:** The experimental platform uses an M1 chip with 16GB memory, Python 3.10 and Tensorflow 2.10. The pre-trained BERT model is a transformers library version 4.37.2, with the model name ”bert-base-uncased”. The MFCC extraction algorithm uses librosa library.

**Algorithm Settings:**  Adam is chosen as the model optimizer, and the learning rate is set to 0.001. Meanwhile, the training time of the model is set to 100 epochs, and the optimal model parameters are preserved using an early stopping mechanism. The hyper-parameters of the model are set as follows: threshold f ansThre=partThre=1000, decay factor α=0.62/0.68, signal length (number of sampling points) T=5000/7500.

# Datasets Construction

<table>
  <tr>
    <th width="400" >Source</th>
    <th width="900" >Description</th>
    <th width="300" >URL</th>
  </tr>
  <tr>
    <th width="400" >Weibo Community Management Center</th>
    <th width="900" >The official display website for WEIBO. Displayed content is officially reviewed fake news, user dispute judgements and spammer accounts.</th>
    <th width="300" >https://service.account.weibo.com/</th>
  </tr>
  <tr>
    <th width="400" >Spammers Display Platform</th>
    <th width="900" >The official website of WEIBO for displaying spammers' accounts. All displayed accounts are determined based on user submissions and official manual review.</th>
    <th width="300" >https://service.account.weibo.com/toppunish</th>
  </tr>
  <tr>
    <th width="400" >Spam Display Platform</th>
    <th width="900" >The official website of WEIBO for displaying spam (fake news).</th>
    <th width="300" >https://service.account.weibo.com/?type=5\&status=4</th>
  </tr>
  <tr>
    <th width="400" >China Fact Check</th>
    <th width="900" >A platform to fact-check Chinese international news.</th>
    <th width="300" >https://chinafactcheck.com/</th>
  </tr>
  <tr>
    <th width="400" >China Joint Internet Rumor-Busting Platform</th>
    <th width="900" >A joint rumor ( fake news ) display platform launched by the Chinese government. It contains fake news from all social media platforms in China.</th>
    <th width="300" >https://www.piyao.org.cn/</th>
  </tr>
</table>

![示例图片](https://github.com/yzhouli/temp/tree/master/fig/weibo.jpg "示例图片标题")


