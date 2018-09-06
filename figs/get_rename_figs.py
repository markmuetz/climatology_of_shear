"""Download and rename all files."""
import os
import re
import subprocess as sp
import shutil


SERVER = 'mmuetz@login.archer.ac.uk'
LOC = '/nerc/n02/n02/mmuetz/um10.9_runs/archive/u-au197/share/data/history/P1M/figs/./'

FILENAMES = [
    # Need to rerun on ARCHER.
    # ('atmos.None.shear_profile_classification_analysis.PCA_PROFILE_True_cape-shear_magrot_pi-0_evr-0.5278288722038269.png', [(r'_evr.*(?:\.png)', r'')]),
    # ('atmos.None.shear_profile_classification_analysis.PCA_PROFILE_True_cape-shear_magrot_pi-1_evr-0.1835406869649887.png', [(r'_evr.*(?:\.png)', r'')]),
    # ('atmos.None.shear_profile_classification_analysis.PCA_PROFILE_True_cape-shear_magrot_pi-2_evr-0.1671045869588852.png', [(r'_evr.*(?:\.png)', r'')]),
    # ('atmos.None.shear_profile_classification_analysis.PCA_PROFILE_True_cape-shear_magrot_pi-3_evr-0.04120809957385063.png',[(r'_evr.*(?:\.png)', r'')]),
    # ('atmos.None.shear_profile_classification_analysis.PCA_RED_True_cape-shear_magrot_725164_-4_nclust-11_prof-3452.png', None), 
    # ('atmos.None.shear_profile_classification_analysis.PCA_RED_True_cape-shear_magrot_725164_-4_nclust-11_prof-7767.png', None), 
    # ('atmos.None.shear_profile_classification_analysis.PCA_RED_True_cape-shear_magrot_725164_-4_nclust-11_prof-5178.png', None), 
    # ('atmos.None.shear_profile_classification_analysis.PCA_RED_True_cape-shear_magrot_725164_-4_nclust-11_prof-12082.png', None),
    # ('atmos.None.shear_profile_classification_analysis.KMEANS_SCORES_True_cape-shear_magrot.png', None),
    # ('atmos.None.shear_profile_classification_analysis.PROFILES_GEOG_LOC_True_cape-shear_magrot_391137_-4_nclust-11.png', None),
]


def get_all():
    filenames = [os.path.join(LOC, fn[0]) for fn in FILENAMES]

    cmd_filenames = ' :'.join(filenames)
    cmd = f'rsync -Rza {SERVER}:{cmd_filenames} raw/'
    sp.call(cmd, shell=True)


def rename_all():
    for (fn, sub_repl) in FILENAMES:
        new_fn = re.sub('atmos.None.shear_profile_classification_analysis.', '', fn)
        if sub_repl:
            for sub, repl in sub_repl:
                new_fn = re.sub(sub, repl, new_fn) + '.png'
        print(f'{fn} -> {new_fn}')
        shutil.copyfile(os.path.join('raw', fn), new_fn)


def main():
    if not os.path.exists('raw'):
        os.makedirs('raw')

    get_all()
    rename_all()


if __name__ == '__main__':
    main()
