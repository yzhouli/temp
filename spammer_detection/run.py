from model.u2a_msd import User2Audio_MultiFeatureSpammerDetection
from train.u2a_train import User2AudioTrain


def main():
    predict_size = 2
    event_embedding = 768
    self_embedding = 8192
    h_dim = 256
    u2a_msd = User2Audio_MultiFeatureSpammerDetection(self_size=self_embedding, embedding_size=event_embedding,
                                                      out_size=predict_size, h_dim=h_dim)
    dataset_path = ''  # please replace dataset path
    learning_rate = 0.001
    epochs = 100
    batch_size = 2
    time_interval = -1
    normal_size = 29
    event_threshold = 1000
    user_threshold = 1000
    decay_factor = 0.62
    audio_sampling_num = 2500
    hz = 4800
    u2a_train = User2AudioTrain(path_ref=dataset_path, learning_rate=learning_rate, epochs=epochs,
                                batch_size=batch_size, time_interval=time_interval, normal_size=normal_size,
                                event_threshold=event_threshold, user_threshold=user_threshold,
                                decay_factor=decay_factor,
                                audio_sampling_num=audio_sampling_num, hz=hz, model=u2a_msd,
                                event_size=event_embedding)
    acc_max, auc_max = u2a_train.train()


if __name__ == '__main__':
    main()
