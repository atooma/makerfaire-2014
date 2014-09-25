
package com.atooma.plugin.greethumb;

import com.atooma.sdk.AtoomaRegistrationReceiver;

public class GREETHUMBReceiver extends AtoomaRegistrationReceiver {

    @Override
    public Class getRegisterServiceClass() {
        return GREETHUMBRegister.class;
    }

}
