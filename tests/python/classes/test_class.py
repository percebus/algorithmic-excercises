from typing import Any

from hamcrest import assert_that, empty, equal_to, is_, is_not


def test_cls_VS_self_mutable_items_with_same_name() -> None:
    class BadClass:
        __test__ = False

        # cls.items
        items: list[Any] = []

        def __init__(self):
            # hides reference to cls.items
            self.items = []

        @classmethod
        def get_class_items(cls):
            return cls.items

        def get_instance_items(self):
            return self.items

    assert_that(BadClass.items, is_(empty()))

    BadClass.items += [1, 2, 3]
    assert_that(BadClass.items, is_(equal_to([1, 2, 3])))

    badClass1 = BadClass()
    # instance field obscures reference to cls.items
    assert_that(badClass1.items, is_not(equal_to([1, 2, 3])))
    assert_that(badClass1.items, is_(empty()))

    # This does NOT access cls.items
    badClass1.items += [4, 5, 6]
    assert_that(badClass1.items, is_(equal_to([4, 5, 6])))

    badClass2 = BadClass()
    assert_that(badClass2.items, is_(empty()))

    # this does NOT access cls.items, either
    badClass2.items += [7, 8, 9]
    assert_that(badClass2.items, is_(equal_to([7, 8, 9])))

    assert_that(BadClass.get_class_items(), is_(equal_to([1, 2, 3])))
    assert_that(badClass1.get_class_items(), is_(equal_to([1, 2, 3])))
    assert_that(badClass1.get_instance_items(), is_(equal_to([4, 5, 6])))
    assert_that(badClass2.get_instance_items(), is_(equal_to([7, 8, 9])))


def test_cls_VS_self_mutable_items_with_different_names() -> None:
    class GoodClass:
        __test__ = False

        # cls.items
        cls_items: list[Any] = []

        def __init__(self):
            self.obj_items: list[Any] = []

    assert_that(GoodClass.cls_items, is_(empty()))

    goodClass1 = GoodClass()
    assert_that(goodClass1.cls_items, is_(empty()))
    assert_that(goodClass1.obj_items, is_(empty()))

    goodClass2 = GoodClass()
    assert_that(goodClass1.cls_items, is_(empty()))
    assert_that(goodClass1.obj_items, is_(empty()))

    goodClass1.cls_items += [1, 2, 3]
    goodClass1.obj_items += [4, 5, 6]

    goodClass2.cls_items += [4, 5, 6]
    goodClass2.obj_items += [7, 8, 9]

    # cls items can be access directly
    assert_that(GoodClass.cls_items, is_(equal_to([1, 2, 3, 4, 5, 6])))
    assert_that(goodClass1.cls_items, is_(equal_to([1, 2, 3, 4, 5, 6])))
    assert_that(goodClass1.obj_items, is_(equal_to([4, 5, 6])))
    assert_that(goodClass2.cls_items, is_(equal_to([1, 2, 3, 4, 5, 6])))
    assert_that(goodClass2.obj_items, is_(equal_to([7, 8, 9])))
