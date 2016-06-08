Component
=========

Software component.

.. class:: Component

   Definition of a component.
   
   .. function:: available(context)
   
      Check this component is available.
      
      Return True if it is available or False otherwise. But it can also return
      None if availability is not known or it is not relevant.
      
      :param execution.Context context:
         Current execution context.
      :rtype:
         bool
      :return:
         Component availability.
   
   .. function:: insert(context)
   
      Insert this component.
      
      :param execution.Context context:
         Current execution context.
         
   .. function:: delete(context)
   
      Delete this component.
      
      :param execution.Context context:
         Current execution context.

