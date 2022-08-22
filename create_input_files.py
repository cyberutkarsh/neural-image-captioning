from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='/mnt/projects/a-PyTorch-Tutorial-to-Image-Captioning/data/caption_data/dataset_coco.json',
                       image_folder='/mnt/projects/a-PyTorch-Tutorial-to-Image-Captioning/data/images/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/mnt/projects/a-PyTorch-Tutorial-to-Image-Captioning/data/',
                       max_len=50)
