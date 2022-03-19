''' Contains format strings for various SMS notifications '''
MSGTEMPL_TV_SHOW_READY = \
    '{tv_show_name} S{season_number}E{episode_number}: {episode_title} ' + \
    'is now available to watch on {server_name}!'
MSGTEMPL_TV_SHOW_MULTI_READY = \
    '{episode_list} from {tv_show_name} are now available to ' + \
    'watch on {server_name}'
MSGTEMPL_MOVIE_READY = \
    '{movie_name} ({movie_year}) is now available to watch on {server_name}!'