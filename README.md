# Experimental Settings

**Platform Settings:** The experimental platform uses an M1 chip with 16GB memory, Python 3.10 and Tensorflow 2.10. The pre-trained BERT model is a transformers library version 4.37.2, with the model name ”bert-base-uncased”. The MFCC extraction algorithm uses librosa library.

**Algorithm Settings:**  Adam is chosen as the model optimizer, and the learning rate is set to 0.001. Meanwhile, the training time of the model is set to 100 epochs, and the optimal model parameters are preserved using an early stopping mechanism. The hyper-parameters of the model are set as follows: threshold f ansThre=partThre=1000, decay factor α=0.62/0.68, signal length (number of sampling points) T=5000/7500.

# Datasets Construction

<table width="500">
  <tr>
    <th width="500" >Source</th>
    <th width="500" >Description</th>
    <th width="500" >URL</th>
  </tr>
  <tr>
    <td>Data 1</td>
    <td>Data 2</td>
    <td>Data 3</td>
  </tr>
</table>

\begin{table*}[!ht]
	\centering
		\begin{tabular}{p{0.2\linewidth}|p{0.45\linewidth}|p{0.25\linewidth}}\toprule[1.5pt]
			Source & Description & URL  \\ \hline \hline
			Weibo Community Management Center & The official display website for WEIBO. Displayed content is officially reviewed fake news, user dispute judgements and spammer accounts. & https://service.account.weibo.com/ \\ \hline
			Spammers Display Platform & The official website of WEIBO for displaying spammers' accounts. All displayed accounts are determined based on user submissions and official manual review. & https://service.account.weibo.com/\ toppunish \\ \hline \hline
			Spam Display Platform & The official website of WEIBO for displaying spam (fake news). & https://service.account.weibo.com/\ ?type=5\&status=4 \\ \hline
			China Fact Check & A platform to fact-check Chinese international news. &  https://chinafactcheck.com/ \\ \hline
			China Joint Internet Rumor-Busting Platform & A joint rumor ( fake news ) display platform launched by the Chinese government. It contains fake news from all social media platforms in China. & https://www.piyao.org.cn/ \\ \hline \hline
			\toprule[1.3pt]
		\end{tabular}
	\caption{Resources used in the collection process}
	\label{table_dataset_1}
\end{table*}
