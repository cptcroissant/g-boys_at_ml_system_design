import numpy as np


def extract_subpart(Z: np.array, shape: np.array) -> list:
    """
    # todo
    :param Z:
    :param shape:
    :return:
    """
    fill = 0
    position = (1, 1)

    R = np.ones(shape, dtype=Z.dtype) * fill
    P = np.array(list(position)).astype(int)
    Rs = np.array(list(R.shape)).astype(int)
    Zs = np.array(list(Z.shape)).astype(int)

    R_start = np.zeros((len(shape),)).astype(int)
    R_stop = np.array(list(shape)).astype(int)
    Z_start = (P - Rs // 2)
    Z_stop = (P + Rs // 2) + Rs % 2

    R_start = (R_start - np.minimum(Z_start, 0)).tolist()
    Z_start = (np.maximum(Z_start, 0)).tolist()
    R_stop = np.maximum(R_start, (R_stop - np.maximum(Z_stop - Zs, 0))).tolist()
    Z_stop = (np.minimum(Z_stop, Zs)).tolist()

    r = [slice(start, stop) for start, stop in zip(R_start, R_stop)]
    z = [slice(start, stop) for start, stop in zip(Z_start, Z_stop)]
    R[r] = Z[z]

    return [R]



def show_user_preview(df_faces, age, sex, etn) -> None:
    person_idx = df_faces.query(f'age=={age} and gender=={sex} and ethnicity=={etn}').index[np.random.randint(0, 10)]
    base = faces[person_idx]

    r = base.reshape(48, 48).astype(int)
    g = base.reshape(48, 48).astype(int)
    b = base.reshape(48, 48).astype(int)

    np.multiply(r, 0.593, out=r, casting="unsafe")
    np.multiply(g, 0.60, out=g, casting="unsafe")
    np.multiply(b, 0.51, out=b, casting="unsafe")

