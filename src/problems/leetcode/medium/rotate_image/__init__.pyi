from problems.leetcode.medium.rotate_image.typing import MatrixType

def rotate(nums: MatrixType) -> None:
    """Rotate.

    Rotate the image represented by the given matrix by 90 degrees clockwise in place.

    Parameters
    ----------
        - `nums:list[list[int]]`.- The input `matrix` representing the image to be rotated.

    Returns
    -------
        - :result: None:
            - The function modifies the input `matrix` in place and does not return anything.

    Examples
    --------
        - Example 1:
        >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
        >>> rotate(matrix)
        >>> matrix
        [[7,4,1],[8,5,2],[9,6,3]]


        - Example 2:
        >>> matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        >>> rotate(matrix)
        >>> matrix
        [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    """
    ...
