"""Download and rename all files."""
import os
import re
import subprocess as sp
import shutil


SERVER = 'mmuetz@login.archer.ac.uk'
LOC = '/home/n02/n02/mmuetz/nerc/um10.9_runs/archive/u-au197/omnium_output/om_v0.10.3.0_cosar_v0.7.0.0_4021354f15/P5Y_DP20/figs/./'

FILENAMES = [
    ('shear_profile_plot_PROFILES_GEOG_LOC_True_cape-shear_magrot_391137_-7_nclust-10.png', None),
    ('shear_profile_plot_SEVEN_PCA_PROFILES_True_cape-shear.png', None),
    ('shear_profile_plot_PROFILES_GEOG_ALL_True_cape-shear_magrot_391137_-7_nclust-10.png', None),
    ('shear_profile_plot_ALL_PROFILES_True_cape-shear_magrot_391137_-7_nclust-10.png', None),
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
