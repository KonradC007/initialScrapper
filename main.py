import python_package
from multiprocessing import Pool
import processVideo


def main():
    file_path = "tmp/results.json"
    table_id = "thunderz-344909.youtube_search.search_results"
    bq_client = python_package.Bigquery_connection()
    channels = bq_client.bq_query(query="SELECT * FROM `thunderz-344909.youtube_search.search_results`")
    transform = python_package.Transform()

    if __name__ == '__main__':
        with Pool(50) as p:
            channels_list = p.map(processVideo.process_video, channels)
            df_channel = transform.list_of_dicts_to_df(list_of_dicts=channels_list)

    bq_client.import_data_to_bq_df(df=df_channel, table_id="thunderz-344909.youtube_search.yt_initial_data")


if __name__ == '__main__':
    main()
