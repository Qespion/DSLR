# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oespion <oespion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/08/18 18:10:55 by oespion           #+#    #+#              #
#    Updated: 2018/08/18 18:44:45 by oespion          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt

def draw_histograms(df, variables, n_rows, n_cols):
    fig=plt.figure()
    for i, var_name in enumerate(variables):
        ax=fig.add_subplot(n_rows,n_cols,i+1)
        df[var_name].hist(bins=10,ax=ax)
        ax.set_title(var_name+" Distribution")
    fig.tight_layout()
    plt.show()

test = DataFrame(np.random.randn(30, 9), columns=map(str, range(9)))
draw_histograms(test, test.columns, 3, 3)
