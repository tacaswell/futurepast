import warnings
import functools


def _attach_class_warning(Class, message):
    original_init = Class.__init__

    @functools.wraps(original_init)
    def deprecated_init(*args, **kwargs):
        warnings.warn(message, category=UserWarning)
        return original_init(*args, **kwargs)

    Class.__init__ = deprecated_init
    Class._deprecated = True
    old_doc = Class.__doc__
    Class.__doc__ = "*DEPRECATED*\n\n"
    # maybe __doc__ was None
    if old_doc:
        Class.__doc__ += old_doc
    return Class
