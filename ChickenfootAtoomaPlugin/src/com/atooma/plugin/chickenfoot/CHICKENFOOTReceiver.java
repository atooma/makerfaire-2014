
package com.atooma.plugin.chickenfoot;

import com.atooma.sdk.AtoomaRegistrationReceiver;

public class CHICKENFOOTReceiver extends AtoomaRegistrationReceiver {

    @Override
    public Class getRegisterServiceClass() {
        return CHICKENFOOTRegister.class;
    }

}
