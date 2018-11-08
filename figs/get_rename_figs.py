"""Download and rename all files."""
import os
import re
import subprocess as sp
import shutil


SERVER = 'mmuetz@login.archer.ac.uk'
LOC_OLD = '/home/n02/n02/mmuetz/nerc/um10.9_runs/archive/u-au197/omnium_output/om_v0.10.3.0_cosar_v0.7.0.0_4021354f15/P5Y_DP20/figs/./'
LOC_SENS_FAVOUR_LOWER_TROP_FAVOUR = '/home/n02/n02/mmuetz/nerc/um10.9_runs/archive/u-au197/omnium_output/om_v0.11.0.0_cosar_v0.7.0.0_4021354f15/P5Y_DP20/figs/./'
LOC_SENS_FAVOUR_LOWER_TROP_NO_FAVOUR = '/home/n02/n02/mmuetz/nerc/um10.9_runs/archive/u-au197/omnium_output/om_v0.11.0.0_cosar_v0.7.0.0_79dc400533/P5Y_DP20/figs/./'

LOC_COSAR_TMP = '/home/n02/n02/mmuetz/nerc/um10.9_runs/archive/u-au197/archived_omnium_output/omnium_output/om_v0.11.0.0_cosar_v0.7.1.0_e889d0f4f8/P5Y_DP20/figs/./'
LOC_COSAR_0_7_3_0_RC1 = '/home/n02/n02/mmuetz/nerc/um10.9_runs/archive/u-au197/omnium_output/om_v0.11.1.0_cosar_v0.7.3.0_e889d0f4f8/P5Y_DP20/figs/./'

OLD_FILENAMES = [
    (LOC_OLD, 'shear_profile_plot_PROFILES_GEOG_LOC_True_cape-shear_magrot_391137_-7_nclust-10.png', None, None),
    (LOC_OLD, 'shear_profile_plot_SEVEN_PCA_PROFILES_True_cape-shear.png', None, None),
    (LOC_OLD, 'shear_profile_plot_PROFILES_GEOG_ALL_True_cape-shear_magrot_391137_-7_nclust-10.png', None, None),
    (LOC_OLD, 'shear_profile_plot_ALL_PROFILES_True_cape-shear_magrot_391137_-7_nclust-10.png', None, None),
    (LOC_SENS_FAVOUR_LOWER_TROP_FAVOUR, 'shear_profile_plot_PROFILES_GEOG_LOC_True_cape-shear_magrot_391137_-7_nclust-10.png', None, 'sens_favour_lower_'),
    (LOC_SENS_FAVOUR_LOWER_TROP_NO_FAVOUR, 'shear_profile_plot_PROFILES_GEOG_LOC_True_cape-shear_magrot_391137_-10_nclust-10.png', None, 'sens_no_favour_lower_'),
]

FILENAMES = [
    (LOC_COSAR_TMP, 'shear_profile_plot_RWP_month_hist_391137.pdf', None, None),
]


def get_all():
    filenames = [os.path.join(*fn[:2]) for fn in FILENAMES]

    cmd_filenames = ' :'.join(filenames)
    cmd = f'rsync -Rza {SERVER}:{cmd_filenames} raw/'
    sp.call(cmd, shell=True)


def rename_all():
    for (loc, fn, sub_repl, prefix) in FILENAMES:
        new_fn = re.sub('atmos.None.shear_profile_classification_analysis.', '', fn)
        if sub_repl:
            for sub, repl in sub_repl:
                new_fn = re.sub(sub, repl, new_fn) + '.png'
        if prefix:
            new_fn = prefix + new_fn
        print(f'{fn} -> {new_fn}')
        shutil.copyfile(os.path.join('raw', fn), new_fn)


def main():
    if not os.path.exists('raw'):
        os.makedirs('raw')

    get_all()
    rename_all()


if __name__ == '__main__':
    main()
