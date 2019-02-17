


label protoype_end:
    "That's it for this protoype."
    return





label affectionasignment:
    $ n_modappealstored = n_modappealstored + n_modappeal
    $ s_modappealstored = s_modappealstored + s_modappeal
    $ y_modappealstored = y_modappealstored + y_modappeal
    $ m_modappealstored = m_modappealstored + m_modappeal
    $ n_modappeal = 0
    $ s_modappeal = 0
    $ y_modappeal = 0
    $ m_modappeal = 0
